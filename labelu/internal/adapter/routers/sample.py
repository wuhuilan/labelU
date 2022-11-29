from typing import List, Union

from pydantic import Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, Security
from fastapi.responses import FileResponse
from fastapi.security import HTTPAuthorizationCredentials

from labelu.internal.common import db
from labelu.internal.common.security import security
from labelu.internal.common.error_code import ErrorCode
from labelu.internal.common.error_code import UnicornException
from labelu.internal.domain.models.user import User
from labelu.internal.dependencies.user import get_current_user
from labelu.internal.application.service import sample as service
from labelu.internal.application.command.sample import PatchSampleCommand
from labelu.internal.application.command.sample import CreateSampleCommand
from labelu.internal.application.command.sample import DeleteSampleCommand
from labelu.internal.application.response.base import OkResp
from labelu.internal.application.response.base import CommonDataResp
from labelu.internal.application.response.sample import SampleResponse
from labelu.internal.application.response.sample import CreateSampleResponse


router = APIRouter(prefix="/tasks", tags=["samples"])


@router.post(
    "/{task_id}/samples",
    response_model=OkResp[CreateSampleResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create(
    task_id: int,
    cmd: List[CreateSampleCommand],
    authorization: HTTPAuthorizationCredentials = Security(security),
    db: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Create a sample.
    """

    # business logic
    data = await service.create(
        db=db, task_id=task_id, cmd=cmd, current_user=current_user
    )

    # response
    return OkResp[CreateSampleResponse](data=data)


# TODO: meta data
@router.get(
    "/{task_id}/samples",
    response_model=OkResp[List[SampleResponse]],
    status_code=status.HTTP_200_OK,
)
async def list(
    after: Union[int, None] = None,
    before: Union[int, None] = None,
    pageNo: Union[int, None] = None,
    pageSize: Union[int, None] = 100,
    authorization: HTTPAuthorizationCredentials = Security(security),
    db: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Get a annotation result.
    """
    if [bool(i) for i in [after, before, pageNo]].count(True) != 1 and pageNo != 0:
        raise UnicornException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            code=ErrorCode.CODE_51000_SAMPLE_LIST_PARAMETERS_ERROR,
        )

    # business logic
    data = await service.list(
        db=db,
        after=after,
        before=before,
        pageNo=pageNo,
        pageSize=pageSize,
        current_user=current_user,
    )

    # response
    return OkResp[List[SampleResponse]](data=data)


@router.get(
    "/{task_id}/samples/{sample_id}",
    response_model=OkResp[SampleResponse],
    status_code=status.HTTP_200_OK,
)
async def get(
    sample_id: int,
    authorization: HTTPAuthorizationCredentials = Security(security),
    db: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Get a annotation result.
    """

    # business logic
    data = await service.get(db=db, sample_id=sample_id, current_user=current_user)

    # response
    return OkResp[SampleResponse](data=data)


@router.patch(
    "/{task_id}/samples/{sample_id}",
    response_model=OkResp[SampleResponse],
    status_code=status.HTTP_200_OK,
)
async def update(
    sample_id: int,
    cmd: PatchSampleCommand,
    authorization: HTTPAuthorizationCredentials = Security(security),
    db: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    """
    update a annotation.
    """

    # business logic
    data = await service.patch(
        db=db, sample_id=sample_id, cmd=cmd, current_user=current_user
    )

    # response
    return OkResp[SampleResponse](data=data)


@router.delete(
    "/{task_id}/samples",
    response_model=OkResp[CommonDataResp],
    status_code=status.HTTP_200_OK,
)
async def delete(
    cmd: DeleteSampleCommand,
    authorization: HTTPAuthorizationCredentials = Security(security),
    db: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    """
    delete a annotation.
    """

    # business logic
    data = await service.delete(
        db=db, sample_ids=cmd.sample_ids, current_user=current_user
    )

    # response
    return OkResp[CommonDataResp](data=data)


@router.get(
    "/{task_id}/samples/export",
    response_class=FileResponse,
    status_code=status.HTTP_200_OK,
)
async def export(
    task_id: int,
    export_type: str,
    sample_ids: List[int],
    authorization: HTTPAuthorizationCredentials = Security(security),
    db: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    """
    export data.
    """

    # business logic
    data = await service.export(
        db=db,
        task_id=task_id,
        export_type=export_type,
        sample_ids=sample_ids,
        current_user=current_user,
    )

    # response
    return data
