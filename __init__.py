from .PIPCutImage import PIPCutImage
from .PIPMergeImage import PIPMergeImage

NODE_CLASS_MAPPINGS = {
    "PIPCutImage": PIPCutImage,
    "PIPMergeImage": PIPMergeImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PIPCutImage": "PIP 图像裁切",
    "PIPMergeImage": "PIP 图像拼接"
}
