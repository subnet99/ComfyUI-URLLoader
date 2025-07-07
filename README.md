# ComfyUI-URLLoader

ComfyUI plugin for downloading and loading media files from URLs.

## Features

### URL Image Loader

- Download images from URLs and convert them to ComfyUI's IMAGE format
- Supports common image formats (JPG, PNG, GIF, etc.)
- Automatic RGB conversion and normalization
- Direct preview in ComfyUI interface

### URL Audio Loader

- Download audio files from URLs and convert them to ComfyUI's AUDIO format
- Supports common audio formats (MP3, WAV, FLAC, etc.)
- Automatic waveform loading with sample rate detection
- Direct playback in ComfyUI interface

## Installation

1. Clone this repository to your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/subnet99/ComfyUI-URLLoader.git
```

2. Restart ComfyUI

## Usage

### Loading Images from URL

1. Add the "Load Image from URL" node to your workflow
2. Enter the image URL in the `url` field
3. The node will download the image and output it in IMAGE format
4. Connect the output to any image processing nodes

### Loading Audio from URL

1. Add the "Load Audio from URL" node to your workflow
2. Enter the audio URL in the `url` field
3. The node will download the audio and output it in AUDIO format
4. Connect the output to any audio processing nodes

## Node Reference

### ImageLoader

- **Input**: `url` (STRING) - The URL of the image to download
- **Output**: `image` (IMAGE) - The downloaded image as a tensor
- **Category**: utils

### AudioLoader

- **Input**: `url` (STRING) - The URL of the audio file to download
- **Output**: `audio` (AUDIO) - The downloaded audio as waveform data
- **Category**: utils

## Dependencies

- No additional dependencies required
- Uses Python standard library (urllib) for URL downloads
- Other dependencies (torch, numpy, Pillow, torchaudio) are typically included with ComfyUI

## Notes

- All downloaded files are saved to ComfyUI's input directory
- The plugin uses a custom User-Agent to avoid download restrictions
- Images are automatically converted to RGB format and normalized to [0, 1]
- Audio files are loaded with their original sample rate preserved
- HTTPS URLs are recommended for secure downloads

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Issues

If you encounter any issues, please report them on the GitHub repository.
