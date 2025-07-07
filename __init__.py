from .image_loader import ImageLoader
from .audio_loader import AudioLoader

NODE_CLASS_MAPPINGS = {
    "ImageLoader": ImageLoader,
    "AudioLoader": AudioLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageLoader": "Load Image from URL",
    "AudioLoader": "Load Audio from URL"
} 