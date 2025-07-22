import gradio as gr
from PIL import Image
from transformers import pipeline
import os
from dotenv import load_dotenv

# Load environment variables (optional, for API-based models)
load_dotenv()

# Initialize Hugging Face BLIP models for image captioning and visual question answering
try:
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    vqa_pipeline = pipeline("visual-question-answering", model="Salesforce/blip-vqa-base")
except Exception as e:
    print(f"Error loading models: {e}")
    exit(1)

# Function to process image and answer questions
def answer_question(image, question):
    if not image or not question:
        return "Please upload an image and enter a question."
    
    # Generate a general description of the image
    try:
        description = image_to_text(image)[0]['generated_text']
    except Exception as e:
        return f"Error processing image: {e}"
    
    # Answer the specific question
    try:
        result = vqa_pipeline(image, question, top_k=1)[0]
        print("VQA Output:", result)  # Debug: Print the model output
        # Check if 'score' exists, else use a default or skip
        confidence = result.get('score', 'N/A')
        if confidence == 'N/A':
            return f"Image Description: {description}\nAnswer: {result['answer']}"
        else:
            return f"Image Description: {description}\nAnswer: {result['answer']} (Confidence: {confidence:.2f})"
    except Exception as e:
        return f"Error answering question: {e}"

# Gradio interface
iface = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.Image(type="pil", label="Upload Image (.jpg or .png)"),
        gr.Textbox(label="Ask a Question")
    ],
    outputs="text",
    title="ImageDescriber - Ask Questions About Your Image",
    description="Upload a .jpg or .png image and ask questions about its content!"
)

# Launch the app
if __name__ == "__main__":
    iface.launch()