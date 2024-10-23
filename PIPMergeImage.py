import cv2
import numpy as np
import torch

class PIPMergeImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_image_a": ("IMAGE",),
                "input_image_b": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_out",)
    CATEGORY = "PIP 图像拼接"
    FUNCTION = "merge_images"

    def merge_images(self, input_image_a, input_image_b):
        # 调试输出：检查输入图像的形状
        print(f"Image A original shape: {input_image_a.shape}")
        print(f"Image B original shape: {input_image_b.shape}")

        # 调整维度顺序：从 [B, H, W, C] 到 [B, C, H, W]
        image_a = input_image_a.permute(0, 3, 1, 2)
        image_b = input_image_b.permute(0, 3, 1, 2)

        # 调试输出：检查调整后的形状
        print(f"Image A adjusted shape: {image_a.shape}")
        print(f"Image B adjusted shape: {image_b.shape}")

        # 获取维度信息
        batch_size_a, channels_a, height_a, width_a = image_a.shape
        batch_size_b, channels_b, height_b, width_b = image_b.shape

        # 调试输出：打印图像的基本信息
        print(f"Image A - Batch: {batch_size_a}, Channels: {channels_a}, Height: {height_a}, Width: {width_a}")
        print(f"Image B - Batch: {batch_size_b}, Channels: {channels_b}, Height: {height_b}, Width: {width_b}")

        # 确保两张图片的高度相同
        if height_a != height_b:
            raise ValueError("输入图像的高度不一致")

        # 计算图像 B 的切片宽度
        part_width_b = width_b // 8

        # 切割图像 B
        parts_b = [image_b[:, :, :, i*part_width_b:(i+1)*part_width_b] for i in range(8)]

        # 调试输出：检查切片的形状
        for i, part in enumerate(parts_b):
            print(f"Part B{i+1} shape: {part.shape}")

        # 计算合并后的宽度
        merged_width = width_a + (6 * part_width_b)  # a1到a8 + b2到b7

        # 创建新的白底图像张量
        merged_tensor = torch.ones((batch_size_a, channels_a, height_a, merged_width), 
                                 dtype=torch.float32)

        # 复制图像 A
        merged_tensor[:, :, :, :width_a] = image_a

        # 复制图像 B 的 b2 到 b7 部分
        for i in range(6):
            start_x = width_a + (i * part_width_b)
            end_x = start_x + part_width_b
            merged_tensor[:, :, :, start_x:end_x] = parts_b[i + 1]

        # 将张量转换回原始格式 [B, H, W, C]
        output_tensor = merged_tensor.permute(0, 2, 3, 1)

        # 调试输出：检查输出张量的形状
        print(f"Output tensor shape: {output_tensor.shape}")

        return (output_tensor,)

# 包含所有要导出的节点的字典，以及它们的名称
NODE_CLASS_MAPPINGS = {
    "PIPMergeImage": PIPMergeImage
}

# 包含节点的友好/人类可读标题的字典
NODE_DISPLAY_NAME_MAPPINGS = {
    "PIPMergeImage": "PIP 图像拼接"
}
