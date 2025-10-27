# Python HTTP Library Demo

This repository contains Jupyter notebooks demonstrating basic HTTP requests, specifically interacting with the OpenAI API, and an introduction to data manipulation using Pandas.

## Project Structure

- `.gitignore`: Specifies intentionally untracked files to ignore (e.g., `.env`, virtual environments).
- `.env`: (Not committed to version control) Used to store environment variables, such as API keys.
- `http-test.ipynb`: A Jupyter notebook that showcases how to make a POST request to the OpenAI Chat Completions API. It retrieves the API key from the `OPEN_AI_SK` environment variable.
- `main.ipynb`: A Jupyter notebook providing a brief introduction and examples of using the Pandas library for data handling.
- `README.md`: This file, providing an overview of the project.

## Features

- **OpenAI API Integration**: Demonstrates making secure API calls to OpenAI's `gpt-4o-mini` model using the `requests` library.
- **Environment Variable Management**: Utilizes `python-dotenv` to load API keys and other sensitive information from a `.env` file, keeping them out of source control.
- **Pandas Basics**: Includes examples of fundamental data structures and operations in the Pandas library.
- **Jupyter Notebooks**: Interactive environment for code execution, documentation, and visualization.

## Requirements

- Python 3.8+ (The project was developed with Python 3.12.9, but newer versions should also work.)
- Recommended Python packages:
  - `requests`
  - `python-dotenv`
  - `pandas`
  - `jupyter` (or `ipython` for notebook execution in VS Code)

## Quick Setup (Linux)

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/py-http.git
    cd py-http
    ```
    *(Note: Replace `https://github.com/your-username/py-http.git` with the actual repository URL if different.)*

2.  **Create and activate a virtual environment** (recommended for dependency management):
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install required packages**:
    ```bash
    pip install requests python-dotenv pandas jupyter
    ```

4.  **Create a `.env` file**: In the root directory of the project (`/home/jonee/Documents/Repos/py-http`), create a file named `.env` and add your OpenAI API key:
    ```
    OPEN_AI_SK=your_openai_secret_key_here
    ```
    Replace `your_openai_secret_key_here` with your actual OpenAI API key.

## Usage

1.  **Open the notebooks**:
    -   You can launch Jupyter Lab or Jupyter Notebook from your terminal:
        ```bash
        jupyter notebook
        ```
        Then navigate to `http-test.ipynb` or `main.ipynb`.
    -   Alternatively, open the project folder in Visual Studio Code and open the `.ipynb` files directly in the built-in notebook editor.

2.  **Run cells**: Execute the cells within the notebooks to see the code in action.
    -   `http-test.ipynb` will make an API call to OpenAI and display the assistant's response. Ensure your `OPEN_AI_SK` is correctly set in `.env`.
    -   `main.ipynb` will demonstrate Pandas operations.

## Security Notes

-   **Never commit your `.env` file or any sensitive API keys directly to version control.** The `.gitignore` file is configured to prevent `.env` from being tracked by Git.
-   Ensure your API keys are kept confidential.

## Notes

-   The notebooks are designed as minimal, self-contained examples for learning and experimentation.
-   Adjust Python versions and package installations as needed for your specific environment.