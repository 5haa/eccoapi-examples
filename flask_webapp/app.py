# =============================================================================
# EccoAPI Flask Webapp Example
# =============================================================================
# A complete Flask web application demonstrating how to use EccoAPI for image
# generation. It supports all playground features:
#   - Text-to-Image: Generate images from text prompts
#   - Image-to-Image: Edit/transform existing images using prompts
#   - Multiple reference images (Pro model only, up to 14)
#   - Pro-only features: imageSize (1K/2K/4K), Google Search grounding
#
# SETUP:
# 1. pip install -r requirements.txt
# 2. Update API_KEY and API_BASE_URL below
# 3. python app.py
# 4. Open http://localhost:5000
# =============================================================================

import base64
import requests
from flask import Flask, render_template, request, jsonify

# -----------------------------------------------------------------------------
# CONFIGURATION - Update these values before running
# -----------------------------------------------------------------------------

# Your EccoAPI key. Get one from your dashboard.
API_KEY = "YOUR_API_KEY_HERE"

# Base URL for the EccoAPI endpoint.
API_BASE_URL = "https://eccoapi.com"

# -----------------------------------------------------------------------------
# FLASK APP
# -----------------------------------------------------------------------------

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main page."""
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    """
    Generate an image using EccoAPI.
    
    Expects JSON body with:
      - prompt: str (required) - The text description
      - model: str (optional) - 'nanobanana' or 'nanobananapro'
      - aspectRatio: str (optional) - e.g., '1:1', '16:9', '9:16', '4:3', '3:4'
      - imageSize: str (optional, Pro only) - '1K', '2K', or '4K'
      - useGoogleSearch: bool (optional, Pro only) - Enable Google Search grounding
      - images: list (optional) - Array of base64 encoded images for reference
          Each item: { data: str, mimeType: str }
    
    Returns JSON with:
      - success: bool
      - image: str (base64 encoded result image)
      - error: str (if failed)
    """
    try:
        data = request.get_json()
        
        # Get parameters
        prompt = data.get("prompt", "").strip()
        model = data.get("model", "nanobanana")
        aspect_ratio = data.get("aspectRatio", "1:1")
        image_size = data.get("imageSize", "1K")  # Pro only
        use_google_search = data.get("useGoogleSearch", False)  # Pro only
        input_images = data.get("images", [])  # Array of {data, mimeType}
        
        if not prompt:
            return jsonify({"success": False, "error": "Prompt is required"})
        
        # Build API request body
        body = {
            "prompt": prompt,
            "aspectRatio": aspect_ratio,
        }
        
        # Add Pro-only parameters if using Pro model
        if model == "nanobananapro":
            body["imageSize"] = image_size
            body["useGoogleSearch"] = use_google_search
        
        # Add input images for image-to-image mode
        # Supports multiple images for Pro model (up to 14)
        if input_images:
            body["imageBase64"] = input_images
        
        # Call EccoAPI
        url = f"{API_BASE_URL}/api/v1/{model}/generate"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        
        response = requests.post(url, json=body, headers=headers)
        result = response.json()
        
        if response.status_code != 200:
            error_msg = result.get("msg", "API request failed")
            return jsonify({"success": False, "error": error_msg})
        
        # Extract image from response
        # Path: data.candidates[0].content.parts[].inlineData.data
        candidates = result.get("data", {}).get("candidates", [])
        
        if not candidates:
            return jsonify({"success": False, "error": "No image generated"})
        
        parts = candidates[0].get("content", {}).get("parts", [])
        
        for part in parts:
            inline_data = part.get("inlineData", {})
            if inline_data.get("data"):
                return jsonify({
                    "success": True,
                    "image": inline_data["data"],
                    "mimeType": inline_data.get("mimeType", "image/png"),
                    "meta": result.get("meta", {})
                })
        
        return jsonify({"success": False, "error": "No image data in response"})
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    print("=" * 60)
    print("EccoAPI Flask Webapp")
    print("=" * 60)
    print(f"API URL: {API_BASE_URL}")
    print(f"Open http://localhost:5000 in your browser")
    print("=" * 60)
    app.run(debug=True, port=5000)
