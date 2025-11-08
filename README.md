# Python HTTP Library Demo - Learning OpenAI API with Jupyter Notebooks

This repository serves as a hands-on guide to interacting with the OpenAI API using Python, specifically through a collection of Jupyter notebooks. Each notebook is designed as a lesson to demonstrate different aspects of the OpenAI API, from chat completions and image generation to audio processing.

## Project Overview

This project contains several Jupyter notebooks for API interaction, designed to be a quick start for understanding common Python HTTP request tasks and exploring various OpenAI models.

## Project Contents

-   `.gitignore`: Configures Git to ignore specified files and directories, such as `.env` and virtual environments.
-   `.env`: (Not tracked by Git) This file is used to store environment variables, particularly sensitive information like API keys.
-   [`chat-completitions.ipynb`](chat-completitions.ipynb): Demonstrates chat completions with various models and role-based prompting.
-   [`dall-e.ipynb`](dall-e.ipynb): Illustrates image generation and variation using the DALL-E 3 model.
-   [`developer-message.ipynb`](developer-message.ipynb): Focuses on using the 'developer' role in chat completions and streaming responses.
-   [`http-test.ipynb`](http-test.ipynb): A Jupyter notebook that demonstrates how to make a raw `POST` request to the OpenAI Chat Completions API using the `requests` library.
-   [`local-image.ipynb`](local-image.ipynb): Explores image analysis by sending local (base64 encoded) and online images to GPT-4o.
-   [`text-to-speech.ipynb`](text-to-speech.ipynb): Shows how to convert text into spoken audio using OpenAI's Text-to-Speech models.
-   [`whisper.ipynb`](whisper.ipynb): Demonstrates audio transcription and translation capabilities using the Whisper model.
-   `README.md`: This document, providing an overview and instructions for the project.
-   `audio/`: Directory for storing generated or input audio files.
-   `images/`: Directory for storing generated or input image files.

## Key Features

-   **OpenAI API Integration**: Illustrates how to send requests to the OpenAI API using both the official `openai` Python library and the `requests` library.
-   **Secure Credential Handling**: Employs `python-dotenv` to load API keys from a `.env` file, preventing them from being hardcoded or committed to version control.
-   **Interactive Development**: Utilizes Jupyter notebooks for an interactive coding and documentation experience, making it easy to experiment with API calls.

## Requirements

-   **Python**: Version 3.8 or higher (tested with Python 3.12.9).
-   **Python Packages**:
    -   `requests`: For making HTTP requests.
    -   `python-dotenv`: For loading environment variables.
    -   `jupyter` (or `ipython`): For running the Jupyter notebooks.
    -   `openai`: The official OpenAI Python client library.
    -   `Pillow` (PIL): For image manipulation (used in DALL-E notebook).

## Setup Instructions (Linux)

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd py-http
    ```
    *(Replace `<repository-url>` with the actual URL of your repository.)*

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install requests python-dotenv jupyter openai pillow
    ```

4.  **Configure API Key**: Create a file named  in the root directory of the project and add your OpenAI API key:
    ```
    OPEN_AI_SK=your_openai_secret_key_here
    ```
    *(Replace `your_openai_secret_key_here` with your actual OpenAI API key.)*

## Usage - Notebook Lessons

Each Jupyter notebook in this repository serves as a self-contained lesson demonstrating a specific aspect of the OpenAI API. To use them:

1.  **Open the notebook**:
    -   Launch Jupyter Notebook from your terminal:
        ```bash
        jupyter notebook
        ```
        Then navigate to and open any of the `.ipynb` files.
    -   Alternatively, open the project folder in Visual Studio Code and use its built-in notebook editor to open the desired `.ipynb` file.

2.  **Execute cells**: Run the code cells within each notebook sequentially. Ensure your `OPEN_AI_SK` is correctly set in your  file.

### 1. Chat Completions ()

*   **Purpose**: This notebook demonstrates how to interact with OpenAI's chat models for generating text. It covers basic chat completion, using different models like  and , and assigning specific roles (e.g., "developer") to influence the model's persona. It also includes an example of listing all available models.
*   **Summary**: Learn the fundamentals of sending prompts to OpenAI's chat API, managing conversational roles, and exploring the range of available models.

### 2. DALL-E Image Generation ()

*   **Purpose**: This lesson focuses on generating images from textual descriptions using the DALL-E 3 model. It shows how to create an image, retrieve its URL, download and save it locally (e.g., to the  directory), and display it. Additionally, it demonstrates how to create variations of an existing image.
*   **Summary**: Master the process of text-to-image generation, image saving, and creating variations using DALL-E.

### 3. Developer Message ()

*   **Purpose**: This notebook highlights advanced features of chat completions, specifically the use of a "developer" role and streaming responses. It provides an example of explaining Object-Oriented Programming with Python, with the response being streamed chunk by chunk.
*   **Summary**: Understand how to leverage specific roles for more controlled outputs and implement real-time streaming for chat responses.

### 4. HTTP Test ()

*   **Purpose**: This notebook provides a foundational understanding of how to interact with the OpenAI API at a lower level, using the `requests` library to make a direct HTTP `POST` request to the chat completions endpoint. It demonstrates constructing headers, JSON payloads, and parsing the API response.
*   **Summary**: Gain insight into the underlying HTTP communication with the OpenAI API, useful for debugging or custom integrations.

### 5. Local Image Processing ()

*   **Purpose**: This lesson explores multimodal capabilities by sending images as input to the  model. It covers encoding local images into base64 for API submission and analyzing images provided via a URL. It also demonstrates how to request responses in multiple languages.
*   **Summary**: Learn to integrate visual input into your prompts, process both local and online images, and handle multilingual outputs from vision models.

### 6. Text-to-Speech ()

*   **Purpose**: This notebook guides you through converting text into natural-sounding speech using OpenAI's Text-to-Speech (TTS) models (e.g., ). It shows how to create an audio file, save it to the  directory, calculate the estimated cost, and play the audio directly within the notebook.
*   **Summary**: Discover how to generate speech from text, manage audio output, and estimate API usage costs for TTS.

### 7. Whisper Audio Processing ()

*   **Purpose**: This lesson demonstrates the power of the Whisper model for audio processing. It covers two main functionalities: transcribing spoken audio into text and translating spoken audio from one language (e.g., German) to another (English).
*   **Summary**: Explore how to accurately convert speech to text and perform language translations on audio files using the Whisper API.
