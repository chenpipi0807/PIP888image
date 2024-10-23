import numpy as np
import torch
from PIL import Image

class PIPCutImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_in": ("IMAGE", {}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_out",)
    CATEGORY = "PIP 图像裁切"
    FUNCTION = "cut_and_rearrange"

    def cut_and_rearrange(self, image_in):
        # 将输入图像转换为 torch tensor
        image_tensor = image_in

        # 调试输出：检查输入图像的形状
        print(f"Original tensor shape: {image_tensor.shape}")

        # 调整维度顺序：从 [B, H, W, C] 到 [B, C, H, W]
        if len(image_tensor.shape) == 4:  # [B, H, W, C]
            image_tensor = image_tensor.permute(0, 3, 1, 2)
        
        # 调试输出：检查调整后的形状
        print(f"Adjusted tensor shape: {image_tensor.shape}")

        # 确保输入图像的通道数大于 0
        if image_tensor.shape[1] == 0:  # 现在通道数在第二个维度
            raise ValueError("输入图像的通道数为 0，请检查输入图像是��正确加载。")

        # 获取维度信息
        batch_size, channels, height, width = image_tensor.shape

        # 调试输出：打印图像的基本信息
        print(f"Batch size: {batch_size}, Channels: {channels}, Height: {height}, Width: {width}")

        # 确保宽度大于等于 8
        if width < 8:
            raise ValueError("图像宽度必须大于等于 8，以便进行切片。")

        # 计算每个切片的宽度
        slice_width = width // 8

        # 切割图像
        slices = [image_tensor[:, :, :, i*slice_width:(i+1)*slice_width] for i in range(8)]

        # 调试输出：检查每个切片的形状
        for i, slice_tensor in enumerate(slices):
            print(f"Slice {i} shape: {slice_tensor.shape}")

        # 创建一个新的黑底图像
        black_background = torch.zeros((batch_size, channels, height, width), dtype=torch.float32)

        # 将 a8 放置在黑底图像最左边，a1 放置在最右边
        black_background[:, :, :, :slice_width] = slices[7]  # a8
        black_background[:, :, :, -slice_width:] = slices[0]  # a1

        # 将 tensor 转换回图像格式 [B, H, W, C]
        output_tensor = black_background.permute(0, 2, 3, 1)

        return output_tensor,

# 包含所有要导出的节点的字典，以及它们的名称
NODE_CLASS_MAPPINGS = {
    "PIPCutImage": PIPCutImage
}

# 包含节点的友好/人类可读标题的字典
NODE_DISPLAY_NAME_MAPPINGS = {
    "PIPCutImage": "PIP 图像裁切"
}
