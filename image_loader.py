import os
from urllib.request import urlopen, Request
from urllib.parse import urlparse
from PIL import Image, ImageOps
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

    RETURN_TYPES = ("IMAGE", "MASK", "PATH")
    RETURN_NAMES = ("image", "mask", "path")
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
            img = Image.open(image_path)
            img = ImageOps.exif_transpose(img)

            if img.mode == "I":
                img = img.point(lambda i: i * (1 / 255))

            # Extract mask from alpha channel before converting to RGB
            if "A" in img.getbands():
                mask = np.array(img.getchannel("A")).astype(np.float32) / 255.0
                mask = 1.0 - torch.from_numpy(mask)
            else:
                h, w = img.size[1], img.size[0]
                mask = torch.zeros((h, w), dtype=torch.float32, device="cpu")

            image = img.convert("RGB")
            image_np = np.array(image, dtype=np.float32) / 255.0
            image_tensor = torch.from_numpy(image_np).unsqueeze(0)

            mask = mask.unsqueeze(0)

            return (image_tensor, mask, image_path)
        except Exception as e:
            raise Exception(f"Image load failed: {e}")
