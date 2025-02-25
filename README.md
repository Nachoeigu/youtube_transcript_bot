# YouTube Transcript Bot

This project is a YouTube Transcript Bot that extracts transcripts from YouTube videos using Selenium.


## Requirements

- Python 3.13
- Selenium
- python-dotenv

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Add your YouTube video URLs to the `links` list in `main.py`.

2. Run the script:
    ```sh
    python main.py
    ```

3. The transcripts will be saved in `output.json`.

## Project Files

- `main.py`: The main script to run the YouTube Transcript Bot.
- `model.py`: Contains the `YoutubeBot` class and related functions.
- `requirements.txt`: Lists the dependencies required for the project.
- `output.json`: The file where the extracted transcripts are saved.
