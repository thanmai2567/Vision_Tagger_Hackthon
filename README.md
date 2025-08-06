# Vision Tagger

## Description

**Vision Tagger** is an AI-powered image tagging and annotation tool that uses machine learning models to automatically tag images with relevant labels. It helps users quickly categorize large datasets of images by applying automatic labels based on the content of each image. The tool leverages the **Google Gemini API** for content generation and analysis.

## Features

- **Automatic Image Tagging:** Tag images automatically based on their content.
- **Customizable Model:** Use pre-trained or custom-trained machine learning models for more accurate tagging.
- **Image Upload:** Upload and process images in multiple formats (PNG, JPG, JPEG).
- **Metadata Extraction:** Extract metadata, such as object labels, descriptions, and attributes.
- **JSON Metadata Download:** Users can download the metadata of the processed images in a JSON format.
- **User-Friendly Interface:** Streamlit-based web interface for seamless interaction.

## Tech Stack

- **Frontend:** Streamlit (Python-based web framework)
- **Backend:** Google Generative AI API (Gemini)
- **Model:** AI model from Google Gemini for content generation and tagging
- **Image Processing:** Pillow (PIL) for image manipulation
- **Environment:** Python 3.x
- **API:** Google Gemini API for image analysis and metadata generation
- **Libraries:** 
  - `streamlit` for the UI
  - `google-generativeai` for accessing the Gemini API
  - `PIL` (Pillow) for handling image uploads and processing
  - `os` and `json` for file handling and environment management

**Set up your Gemini API key:**
    - Create a `.env` file in the project directory and add your Gemini API key:
    ```bash
    GEMINI_API_KEY=your-api-key
streamlit run app.py
    

