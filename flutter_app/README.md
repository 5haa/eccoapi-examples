# EccoAPI Flutter Example

A simple Flutter app demonstrating how to use EccoAPI for AI image generation.

## Features

- **Text-to-Image**: Generate images from text prompts
- **Image-to-Image**: Edit/transform existing images with prompts
- **Aspect Ratio**: Choose from multiple aspect ratios (1:1, 16:9, 9:16, etc.)
- **Save Images**: Download generated images to your device

## Setup

### 1. Get Dependencies

```bash
flutter pub get
```

### 2. Configure API Key

Open `lib/main.dart` and update these values:

```dart
// Your EccoAPI key. Get one from your dashboard.
const String API_KEY = 'YOUR_API_KEY_HERE';

// Base URL for the EccoAPI endpoint.
const String API_BASE_URL = 'https://eccoapi.com';
```

### 3. Run the App

```bash
flutter run
```

## Usage

### Text-to-Image

1. Enter a descriptive prompt (e.g., "a happy dog running in the park")
2. Select an aspect ratio
3. Tap "Generate Image"

### Image-to-Image

1. Tap "Add Image" to select an image from your gallery
2. Enter a prompt describing how to edit the image
3. Tap "Generate Image"

## API Reference

The app calls the EccoAPI endpoint:

```
POST /api/v1/{model}/generate
```

### Request Headers

```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

### Request Body

```json
{
  "prompt": "your image description",
  "aspectRatio": "1:1",
  "imageBase64": [
    {
      "data": "base64_encoded_image",
      "mimeType": "image/jpeg"
    }
  ]
}
```

### Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": {
    "candidates": [
      {
        "content": {
          "parts": [
            {
              "inlineData": {
                "data": "base64_encoded_result_image",
                "mimeType": "image/png"
              }
            }
          ]
        }
      }
    ]
  },
  "meta": {
    "model": "nanobanana",
    "cost": 0.01,
    "remaining_credits": 9.99
  }
}
```

## Available Models

| Model | Cost | Description |
|-------|------|-------------|
| `nanobanana` | $0.01/request | Standard model |
| `nanobananapro` | $0.06/request | Pro model with higher quality |

## Troubleshooting

### "Missing API key"
Make sure to set your API key in `lib/main.dart`.

### "Invalid API key"
Verify your API key is correct and active.

### "Insufficient credits"
Add more credits to your account.

### Image picker not working on iOS
Add these to your `ios/Runner/Info.plist`:
```xml
<key>NSPhotoLibraryUsageDescription</key>
<string>This app needs access to your photo library to select images.</string>
<key>NSCameraUsageDescription</key>
<string>This app needs camera access for taking photos.</string>
```

## License

MIT License - Feel free to use this example in your projects.
