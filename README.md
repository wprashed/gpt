# AI-Powered Web Application

This project is a web-based application developed using Streamlit, Python, and OpenAI's GPT-4 API. It provides various features to help with text manipulation, including rewriting, extending, summarizing, fixing grammar, debugging code, and optimizing code. Additionally, users can download the processed content in various formats such as TXT, PDF, and DOCX.

## Features

- **Text Manipulation**: Users can select from various tasks:
  - **Rewrite**: Rewrite the given text in a new style.
  - **Extend**: Extend the given text with more content.
  - **Summarize**: Summarize the given text into a concise version.
  - **Fix Grammar**: Fix grammatical issues in the provided text.
  - **Fix Code Bug**: Identify and fix any bugs in the provided code.
  - **Optimize Code**: Suggest optimizations for the provided code.
  
- **Text Output**: After processing, the application displays the result in a styled output box.
  
- **Download Options**: Users can download the processed output in the following formats:
  - **TXT**: Download the output as a plain text file.
  - **PDF**: Download the output as a PDF file.
  - **DOCX**: Download the output as a DOCX file.

- **Clipboard Copy**: Users can copy the processed text to their clipboard with a button click.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/wprashed/gpt.git
   ```
   
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that you have an OpenAI API key. You can obtain one by creating an account on [OpenAI](https://platform.openai.com/).

4. Replace the OpenAI API key in the script:
   ```python
   openai.api_key = "your-api-key"
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
   
2. Open the application in your browser. The web app will display options to:
   - Select a task: Rewrite, Extend, Summarize, Fix Grammar, Fix Code Bug, or Optimize Code.
   - Enter your text in the provided text area.
   - Click the "Submit" button to process the text.
   - After processing, the output will be displayed, with options to copy, download as TXT, PDF, or DOCX.

## Code Overview

### Main Components

- **OpenAI API Integration**: 
  The application communicates with OpenAI's GPT-4 model to process the user's input based on the selected task.

- **Text Processing Functions**: 
  Each text manipulation task (e.g., rewrite, extend, summarize, etc.) has its own function that sends the user's input to the OpenAI API and returns the response.

- **Output Display**: 
  The processed text is displayed in a styled output box, and users can download or copy the result.

- **Downloadable Files**:
  The text can be exported as:
  - **PDF**: Created using the `fpdf` library.
  - **DOCX**: Created using the `python-docx` library.
  - **TXT**: A plain text file.

- **User Interface**:
  The interface is built using Streamlit, with custom CSS for styling.

### File Structure

- `app.py`: Main application script.
- `requirements.txt`: List of dependencies required to run the application.
- `assets/`: Folder for any static files (e.g., images or icons).

## Requirements

- Python 3.x
- OpenAI API Key
- Streamlit
- fpdf
- python-docx

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.
