from .image_loader import ImageLoader
from .audio_loader import AudioLoader

NODE_CLASS_MAPPINGS = {
    "URLImageDownloader": ImageLoader,
    "URLAudioDownloader": AudioLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "URLImageDownloader": "Load Image from URL",
    "URLAudioDownloader": "Load Audio from URL",
}
