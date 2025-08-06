# Vision Tagger
A project I'm particularly proud of is Vision Tagger, an AI-powered image tagging and annotation tool designed to automatically generate relevant labels for images. The system utilizes machine learning and computer vision to analyze images, identify objects, and assign appropriate tags, making it easier to categorize large datasets and improve content organization for various use cases.I developed the system using Streamlit for the frontend and Google Generative AI (Gemini API) for image processing, with features like image uploading, automatic tagging, metadata extraction, and downloadable results. A key feature is the AI-powered tagging model, which processes the uploaded images and generates metadata, including object recognition and descriptive labels. The system then presents the metadata in a structured format, allowing users to download it for further analysis or use in various applications.What excites me most about this project is its potential to automate and simplify the image categorization process, reducing manual work and improving efficiency. The ability to analyze images, extract meaningful information, and generate tags quickly opens up numerous possibilities for businesses and researchers working with large image datasets. It was incredibly fulfilling to see how AI could enhance workflows by providing insights from images in a scalable and automated way. This project strengthened my belief in the power of AI to address real-world problems and create intelligent solutions.

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
    

