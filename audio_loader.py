import os
from urllib.request import urlopen, Request
from urllib.parse import urlparse
import torchaudio
import folder_paths

class AudioLoader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "url": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("audio",)
    FUNCTION = "load_from_url"
    CATEGORY = "utils"

    def load_from_url(self, url):
        # Parse filename and construct file path
        filename = os.path.basename(urlparse(url).path)
        audio_path = os.path.join(folder_paths.get_input_directory(), filename)

        # Download audio file using urllib
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            req = Request(url, headers=headers)
            with urlopen(req, timeout=20) as response:
                with open(audio_path, "wb") as f:
                    f.write(response.read())
        except Exception as e:
            raise Exception(f"Audio download failed: {e}")

        # Load audio waveform and sample rate
        try:
            waveform, sample_rate = torchaudio.load(audio_path)
            audio = {"waveform": waveform.unsqueeze(0), "sample_rate": sample_rate}
            return (audio,)
        except Exception as e:
            raise Exception(f"Audio loading failed: {e}") 