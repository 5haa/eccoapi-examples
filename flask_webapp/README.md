# EccoAPI Flask Webapp Example

A simple Flask web application demonstrating how to use EccoAPI for AI image generation.

## Features

- **Text-to-Image**: Generate images from text prompts
- **Image-to-Image**: Edit/transform existing images with prompts
- **Model Selection**: Choose between Nano Banana and Nano Banana Pro
- **Aspect Ratio**: Multiple aspect ratio options
- **Download**: Save generated images locally

## Setup

### 1. Install Dependencies

```bash
cd examples/flask_webapp
pip install -r requirements.txt
```

### 2. Configure API Key

Open `app.py` and update:

```python
API_KEY = "your_api_key_here"
API_BASE_URL = "https://eccoapi.com"
```

### 3. Run the App

```bash
python app.py
```

### 4. Open in Browser

Navigate to: http://localhost:5000

## Usage

1. Enter a descriptive prompt
2. Select a model (Nano Banana or Nano Banana Pro)
3. Choose an aspect ratio
4. Optionally upload an image for image-to-image mode
5. Click "Generate Image"

## API Integration

The webapp calls your EccoAPI backend at:

```
POST /api/v1/{model}/generate
```

### Request Format

```json
{
  "prompt": "your image description",
  "aspectRatio": "1:1",
  "imageBase64": [{
    "data": "base64_encoded_image",
    "mimeType": "image/jpeg"
  }]
}
```

## Project Structure

```
flask_webapp/
├── app.py              # Flask backend
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend UI
└── README.md           # This file
```

## License

MIT License
