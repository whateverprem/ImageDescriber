&nbsp;    # ImageDescriber - GenAI-Powered Image Q\&A



&nbsp;    \*\*ImageDescriber\*\* is a chatbot that lets users upload `.jpg` or `.png` images and ask questions about their content using natural language. Powered by Hugging Face's BLIP models, it generates image descriptions and answers specific questions, like "What objects are in the image?" or "What's the weather like?"



&nbsp;    ## Features

&nbsp;    - Upload `.jpg` or `.png` images and ask questions about their content.

&nbsp;    - Generates image descriptions and answers questions with confidence scores.

&nbsp;    - Built with a user-friendly Gradio web interface.

&nbsp;    - Powered by Hugging Face BLIP models for image captioning and visual question answering.



&nbsp;    ## Demo

&nbsp;    Example usage:

&nbsp;    - \*\*Image\*\*: A beach photo

&nbsp;    - \*\*Question\*\*: "What objects are in the image?"

&nbsp;    - \*\*Output\*\*:

&nbsp;      ```

&nbsp;      Image Description: A sunny beach with waves and seagulls.

&nbsp;      Answer: Waves, seagulls, sand (Confidence: 0.89)

&nbsp;      ```



&nbsp;    ## Tech Stack

&nbsp;    - \*\*Frontend\*\*: Gradio (Python-based UI)

&nbsp;    - \*\*Backend\*\*: Python

&nbsp;    - \*\*Libraries\*\*:

&nbsp;      - `Pillow`: Image processing

&nbsp;      - `transformers`: Hugging Face BLIP models

&nbsp;      - `Gradio`: Web interface

&nbsp;      - `python-dotenv`: Environment variable management



&nbsp;    ## Setup Instructions

&nbsp;    1. \*\*Clone the repository\*\*:

&nbsp;       ```bash

&nbsp;       git clone https://github.com/whateverprem/ImageDescriber.git

&nbsp;       cd ImageDescriber

&nbsp;       ```



&nbsp;    2. \*\*Install dependencies\*\*:

&nbsp;       ```bash

&nbsp;       pip install -r requirements.txt

&nbsp;       ```



&nbsp;    3. \*\*Set up environment variables\*\* (optional):

&nbsp;       Copy `.env.example` to `.env` and add API keys if needed:

&nbsp;       ```bash

&nbsp;       copy .env.example .env

&nbsp;       ```



&nbsp;    4. \*\*Run the app\*\*:

&nbsp;       ```bash

&nbsp;       python app.py

&nbsp;       ```

&nbsp;       Access the Gradio interface at the provided URL (e.g., `http://127.0.0.1:7860`).



&nbsp;    ## How It Works

&nbsp;    - Upload an image via the Gradio interface.

&nbsp;    - The BLIP model generates a general description of the image.

&nbsp;    - Ask a question, and the BLIP visual question-answering model provides an answer with a confidence score.



&nbsp;    ## Notes

&nbsp;    - The BLIP models require ~4GB RAM and an internet connection for initial download.

&nbsp;    - Use clear images for best results.

&nbsp;    - For xAI’s Grok API, check \[xAI API](https://x.ai/api) for setup details.



&nbsp;    ## License

&nbsp;    This project is licensed under the MIT License - see the \[LICENSE](LICENSE) file.

