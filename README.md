# Python HTTP Library Demo

This repository serves as a demonstration of making HTTP requests in Python, specifically interacting with the OpenAI API.

## Project Overview

This project contains a Jupyter notebook for API interaction, designed to be a quick start for understanding common Python HTTP request tasks.

## Project Contents

-   `.gitignore`: Configures Git to ignore specified files and directories, such as `.env` and virtual environments.
-   `.env`: (Not tracked by Git) This file is used to store environment variables, particularly sensitive information like API keys.
-   `http-test.ipynb`: A Jupyter notebook that demonstrates how to make a `POST` request to the OpenAI Chat Completions API. It securely loads the API key from the `OPEN_AI_SK` environment variable defined in `.env`.
-   `README.md`: This document, providing an overview and instructions for the project.

## Key Features

-   **OpenAI API Integration**: Illustrates how to send requests to the OpenAI API using the `requests` library, specifically targeting the `gpt-4o-mini` model.
-   **Secure Credential Handling**: Employs `python-dotenv` to load API keys from a `.env` file, preventing them from being hardcoded or committed to version control.
-   **Interactive Development**: Utilizes Jupyter notebooks for an interactive coding and documentation experience.

## Requirements

-   **Python**: Version 3.8 or higher (tested with Python 3.12.9).
-   **Python Packages**:
    -   `requests`: For making HTTP requests.
    -   `python-dotenv`: For loading environment variables.
    -   `jupyter` (or `ipython`): For running the Jupyter notebooks.

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
    pip install requests python-dotenv jupyter
    ```

4.  **Configure API Key**: Create a file named `.env` in the root directory of the project and add your OpenAI API key:
    ```
    OPEN_AI_SK=your_openai_secret_key_here
    ```
    *(Replace `your_openai_secret_key_here` with your actual OpenAI API key.)*

## Usage

1.  **Open the notebook**:
    -   Launch Jupyter Notebook from your terminal:
        ```bash
        jupyter notebook
        ```
        Then navigate to and open `http-test.ipynb`.
    -   Alternatively, open the project folder in Visual Studio Code and use its built-in notebook editor to open `http-test.ipynb`.

2.  **Execute cells**: Run the code cells within the notebook sequentially.
    -   `http-test.ipynb` will make an API call to OpenAI and display the response. Ensure your `OPEN_AI_SK` is correctly set in your `.env` file.

## Security Considerations

-   **Never commit your `.env` file or any sensitive credentials to version control.** The `.gitignore` file is already configured to prevent this.
-   Always treat your API keys as confidential information.

## Notes

-   The provided notebook is a minimal example intended for educational purposes and quick experimentation.
-   Feel free to adapt the Python version and package installations to suit your specific development environment.