from .image_loader import ImageLoader
from .audio_loader import AudioLoader

__version__ = "0.2.0"

NODE_CLASS_MAPPINGS = {
    "URLImageDownloader": ImageLoader,
    "URLAudioDownloader": AudioLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "URLImageDownloader": "Load Image from URL",
    "URLAudioDownloader": "Load Audio from URL",
}
