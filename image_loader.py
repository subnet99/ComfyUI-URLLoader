import os
from urllib.request import urlopen, Request
from urllib.parse import urlparse
from PIL import Image
import numpy as np
import torch
import folder_paths

class ImageLoader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "url": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "load_from_url"
    CATEGORY = "utils"

    def load_from_url(self, url):
        # Parse filename from URL and construct file path
        filename = os.path.basename(urlparse(url).path)
        image_path = os.path.join(folder_paths.get_input_directory(), filename)

        # Download image file using urllib
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            req = Request(url, headers=headers)
            with urlopen(req, timeout=15) as response:
                with open(image_path, "wb") as f:
                    f.write(response.read())
        except Exception as e:
            raise Exception(f"Image download failed: {e}")

        # Load image as tensor in shape (1, H, W, C), normalized to [0, 1]
        try:
            image = Image.open(image_path).convert("RGB")
            image_np = np.array(image, dtype=np.float32) / 255.0
            image_tensor = torch.from_numpy(image_np).unsqueeze(0)
            return (image_tensor,)
        except Exception as e:
            raise Exception(f"Image load failed: {e}") 