# PIP888image
![微信截图_20241023151628](https://github.com/user-attachments/assets/00c554f5-102a-41eb-bbcf-8d3fa84bd044)

自用节点，八等分切图和拼图
# PIP 图像处理节点

这是一个用于 ComfyUI 的自定义节点集合，专门用于处理 PIP（画中画）图像效果。

## 功能特点

### PIP 图像裁切 (PIPCutImage)
- 将输入图像等分为8份
- 将第8份放置在新图像的最左侧
- 将第1份放置在新图像的最右侧
- 中间区域填充黑色背景
- 支持批处理和多通道图像

### PIP 图像拼接 (PIPMergeImage)
- 接收两张输入图像
- 将第二张图像的中间6个部分（b2到b7）拼接到第一张图像后面
- 保持图像质量和比例
- 自动处理不同尺寸的输入图像

## 安装说明

1. 将本项目克隆或下载到 ComfyUI 的 `custom_nodes` 目录下：

2.克隆项目

cd ComfyUI/custom_nodes
git clone https://github.com/chenpipi0807/PIP888image.git
cd PIP888image
pip install -r requirements.txt


3. 重启 ComfyUI

## 使用方法

### PIP 图像裁切节点
1. 在 ComfyUI 中找到 "PIP 图像裁切" 节点
2. 连接输入图像
3. 节点将自动处理图像并输出结果

### PIP 图像拼接节点
1. 在 ComfyUI 中找到 "PIP 图像拼接" 节点
2. 连接两张输入图像（需要高度相同）
3. 节点将自动完成拼接并输出结果

## 注意事项

- 输入图像的宽度必须大于等于 8 像素
- 拼接时两张图像的高度必须相同
- 建议使用分辨率较高的图像以获得更好的效果
- 所有处理都在 GPU 上进行（如果可用）

## 问题反馈

如果遇到任何问题或有改进建议，请通过以下方式反馈：
- 在 GitHub 上提交 Issue
- 发送邮件至：[您的邮箱]

## 许可证

MIT License

## 作者

PIP888

## 更新日志

### v1.0.0 (2024-01-20)
- 初始版本发布
- 实现基础的图像裁切和拼接功能
