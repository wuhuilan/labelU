 简体中文 | <a href="./GUIDE.md" >English</a>

# 概念

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width=500
 style='width:375.0pt;border-collapse:collapse'>
 <tr style='height:29.25pt'>
  <td style='border-top:solid #DEE0E3 1.0pt;border-left:solid #DEE0E3 1.0pt;
  border-bottom:none;border-right:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:10.0pt;font-family:宋体'>概念</span></b></p>
  </td>
  <td style='border:solid #DEE0E3 1.0pt;border-bottom:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  style='font-size:10.0pt;font-family:宋体'>说明</span></b></p>
  </td>
 </tr>
 <tr style='height:29.25pt'>
  <td style='border-top:solid #DEE0E3 1.0pt;border-left:solid #DEE0E3 1.0pt;
  border-bottom:none;border-right:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>任务（<span lang=EN-US>task</span>）</span></p>
  </td>
  <td style='border:solid #DEE0E3 1.0pt;border-bottom:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>为了对某个数据集进行标注而建立的任务</span></p>
  </td>
 </tr>
 <tr style='height:29.25pt'>
  <td style='border-top:solid #DEE0E3 1.0pt;border-left:solid #DEE0E3 1.0pt;
  border-bottom:none;border-right:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>标签（<span lang=EN-US>label</span>）</span></p>
  </td>
  <td style='border:solid #DEE0E3 1.0pt;border-bottom:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>标注时需要添加的分类标识，比如猫、狗、行人、车辆</span></p>
  </td>
 </tr>
 <tr style='height:29.25pt'>
  <td style='border-top:solid #DEE0E3 1.0pt;border-left:solid #DEE0E3 1.0pt;
  border-bottom:none;border-right:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>标记（<span lang=EN-US>annotation</span>）</span></p>
  </td>
  <td style='border:solid #DEE0E3 1.0pt;border-bottom:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>进行一次标注后生成的对象，比如一个矩形框、一个点</span></p>
  </td>
 </tr>
 <tr style='height:29.25pt'>
  <td style='border-top:solid #DEE0E3 1.0pt;border-left:solid #DEE0E3 1.0pt;
  border-bottom:none;border-right:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>属性（<span lang=EN-US>attribute</span>）</span></p>
  </td>
  <td style='border:solid #DEE0E3 1.0pt;border-bottom:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>对标签的进一步描述，比如将某个物体标为车辆后，添加属性<span lang=EN-US>“</span>车辆遮挡率为<span
  lang=EN-US>20%”</span></span></p>
  </td>
 </tr>
 <tr style='height:29.25pt'>
  <td style='border-top:solid #DEE0E3 1.0pt;border-left:solid #DEE0E3 1.0pt;
  border-bottom:none;border-right:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>标注结果（<span lang=EN-US>result</span>）</span></p>
  </td>
  <td style='border:solid #DEE0E3 1.0pt;border-bottom:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>标记<span lang=EN-US>+</span>标签<span lang=EN-US>+</span>属性，一条完整的标注记录</span></p>
  </td>
 </tr>
 <tr style='height:29.25pt'>
  <td style='border:solid #DEE0E3 1.0pt;border-right:none;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>模板（<span lang=EN-US>template</span>）</span></p>
  </td>
  <td style='border:solid #DEE0E3 1.0pt;padding:.75pt .75pt .75pt .75pt;
  height:29.25pt'>
  <p class=MsoNormal align=left style='text-align:left'><span style='font-size:
  10.0pt;font-family:宋体'>对标注任务进行配置时，可参照的配置文件（<span lang=EN-US>XML</span>、<span
  lang=EN-US>JSON</span>、<span lang=EN-US>Yaml</span>）</span></p>
  </td>
 </tr>
</table>

# 注册登录

1. 通过邮箱密码创建账号
2. 登录进入LabelU

# 新建任务

![image](https://user-images.githubusercontent.com/25022954/208387913-9a4a8205-8dfc-423f-997d-5c6f277ec0eb.png)

1. 点击“新建任务”
2. 输入任务名称、任务描述、任务提示，其中任务提示会在标注过程中为标注人员提供提示帮助
3. 点击“下一步”保存基础配置信息，并进入“数据导入”页面

# 数据导入

![image](https://user-images.githubusercontent.com/25022954/208388040-79b49127-adc0-4468-81d6-f78dc6a80a46.png)

目前数据导入仅支持本地数据导入，支持文件或文件夹导入两种方式。
1. 点击上传文件或上传文件夹，上传本地数据
2. 点击“下一步”保存并进入标注配置
3. 若想再次导入数据，可通过点击任务主页中的“数据导入”进入数据导入页面进行导入，导入的数据可在任务主页中进行查看

# 任务配置

在完成基础配置和数据导入配置后，进行标注配置，主要根据任务场景进行工具和标签的配置编辑，以及其他一些参数配置。目前支持Yaml和可视化两种配置方式，两种方式支持联动，并可通过右边页面进行标注主页的预览

## Yaml配置（待完善）

1. 根据任务需求选择模板
2. 自定义修改Yaml配置，包括工具配置修改、标签配置修改、其他配置修改等
3. 点击完成

## 可视化配置

![image](https://user-images.githubusercontent.com/25022954/208390163-e6b34056-a618-485a-8875-38f99741ee68.png)

除采用Yaml方式配置外，也可选择采用可视化方式进行标注配置，配置流程如下：
1. 选择标注类型，目前仅支持图片，后续将支持音视频、点云、文本等类型
2. 选择标注工具，支持同时配置多种工具（拉框、多边形、标点、标线、分类、描述）
3. 各工具所需配置包括工具属性和标签配置

各工具配置说明：
|工具|配置说明|
|---|---|
|拉框|最小尺寸：拉框最小宽度（W）和高度（H），标签配置：标注对象分类，包括中英文|
|多边形|线条类型：包括直线和曲线，闭合点数：包括最小闭合点数和最大闭合点数，边缘吸附：开启后自动贴合物体边缘，标签配置：标注对象分类，包括中英文|
|标点|上限点数：规定点数上限，超过不可画，标签配置：标注对象分类，包括中英文|
|标线|线条类型：包括直线和曲线，闭合点数：包括最小闭合点数和最大闭合点数，边缘吸附：开启后自动贴合物体边缘，标签配置：标注对象分类，包括中英文|
|文本|文本列表：包括文本描述名称中英文，文本设置：包括最大字数和默认文本|
|分类|类别：分类描述中英文，选项：分类的具体选项中英文|

4. 选择是否支持目标外标注、进行属性配置（目前仅支持文本类型）
5. 设置通用标签（当多工具共用一套标签体系时，可通过设置通用标签简化配置）
6. 预览查看效果
7. 点击保存，进入任务主页

# 开始标注

![image](https://user-images.githubusercontent.com/25022954/208390649-cc0bccb1-c509-4623-aeef-44f6649adc4c.png)

根据任务配置情况开始标注任务，各功能区域介绍如下：
工具栏：进行工具选择、工具样式切换、撤回重做、显示顺序等操作
标签栏：选择工具后单击选择标签进行标注
标注结果栏：对标注的结果进行查看和编辑
标注主体：包括绘图区域、图片操作

标注流程说明：
1. 判断任务是否为无效，若无效点击跳过，进入下一任务
若有效，有绘图任务时（目标检测、语意分割、线标注、点标注），绘图任务时工具和配置的一致
2. 选择工具
3. 选择标签
4. 绘图做标记
5. 弹出属性信息弹窗，编辑属性信息，若无属性信息可不填，点击弹窗外任意处关闭。
6. 在右侧标签结果管理栏单击标签结果可选中图片中对应标记，工具栏中选中工具切换为标签结果的工具。点击标签结果的【编辑】【显示/隐藏】【删除】按钮来管理。
若有效，有标签描述、分类任务时
7. 在右侧结果管理栏填写描述和分类结果
8. 选择[下一页]，进入下一个任务
9. 重复1~8，直到标注完成

各工具具体标注操作详见：

 [图像标注](./labeling/label_image.md) 

# 导出结果

完成标注后，可将标注结果文件以Json形式导出，标注格式说明如下：

[LabelU 标注格式](./annotation%20format/README.md)
