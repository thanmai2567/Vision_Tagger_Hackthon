import streamlit as st
import google.generativeai as genai
import os
import json
from PIL import Image

# Set page configuration at the very top
st.set_page_config(page_title="VisionTagger AI", layout="wide")

# Load API Key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Ensure this is set in your environment

def analyze_image(image_bytes):
    """Function to process image using Gemini API"""
    try:
        model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")
        response = model.generate_content([image_bytes], stream=False)

        if hasattr(response, "text"):
            metadata = response.text
            metadata_json = json.loads(metadata)  # Convert to JSON
            return metadata_json
        else:
            return {"error": "Unexpected API response format."}

    except json.JSONDecodeError:
        return {"error": "Failed to parse API response. Check API output format."}
    except Exception as e:
        return {"error": f"Error processing image: {e}"}

def main():
    if not GEMINI_API_KEY:
        st.error("API Key not found! Please set the GEMINI_API_KEY environment variable.")
        return

    # Configure Gemini API
    genai.configure(api_key=GEMINI_API_KEY)

    # Streamlit UI
    st.title("VisionTagger AI - Image Analysis & Tagging")

    # Image Upload
    uploaded_file = st.file_uploader("📤 Upload an Image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert image to bytes
        image_bytes = uploaded_file.getvalue()

        # Process Image with Gemini
        st.subheader("🔍 Analyzing Image...")
        metadata_json = analyze_image(image_bytes)

        if "error" in metadata_json:
            st.error(f"{metadata_json['error']}")
        else:
            st.json(metadata_json)  # Display JSON output

            # Download JSON metadata
            st.download_button(
                label="📥 Download Metadata",
                data=json.dumps(metadata_json, indent=4),
                file_name="image_metadata.json",
                mime="application/json"
            )

if __name__ == "__main__":
    main()  # Ensures all Streamlit UI functions are inside the main script context
