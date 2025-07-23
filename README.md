# ImageDescriber

📷 **ImageDescriber** is a GenAI-powered chatbot that allows users to upload images (`.jpg` or `.png`) and ask questions about their content using natural language. It provides detailed descriptions of images and answers specific questions, leveraging vision-language models like Hugging Face's BLIP. Perfect for exploring photos, analyzing visuals, or generating creative descriptions!

## 💡 Features
- Upload `.jpg` or `.png` images and ask questions about their content.
- Generates a general description of the image using image captioning.
- Answers specific questions about the image with confidence scores (if available).
- Simple, user-friendly web interface built with Gradio.
- Lightweight and beginner-friendly, using free-tier models.

## 🚀 Tech Stack
- **Frontend**: Gradio (Python-based UI)
- **Backend**: Python
- **Libraries**:
  - `gradio` – Web interface for user interaction
  - `Pillow` – Image processing
  - `transformers` (Hugging Face) – BLIP models for image captioning and visual question answering
  - `python-dotenv` – Environment variable management (optional, for API-based setups)

## 📦 Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ImageDescriber.git
   cd ImageDescriber

2. **Install dependencies**:
   ```bash
   pip install gradio pillow transformers python-dotenv

3. **Run the app**:
   ```bash
   python app.py

4. Open the provided Gradio URL (e.g., http://127.0.0.1:7860) in your browser to access the interface.
