# Getting Started with Speech Recognition in Python

This document will guide you through setting up a Python virtual environment for speech recognition, installing necessary libraries, running a transcription command, and managing your Python installation.
The script will start at the top level of a folder and work down all levels until all files are processed.

NOTE: This uses free software, it runs on your local machine, and none of your data is transferred anywhere else.

**WARNING!** The script was largely written by Google Gemini. It works well for me, but I take no responsibility if anything goes wrong. 
Always take a look at anything you download and run to check it's not doing anything nefarious.


## 1. Creating and Activating a Python Virtual Environment

If you've not got Python installed, there's instructions at the end of this document.

It's good practice to use a virtual environment for your Python projects. This keeps your project dependencies separate from other Python projects and your system-wide Python installation.

1.  **Open your terminal or command prompt.**

2.  **Navigate to your desired project directory.** For example:
    ```bash
    cd C:\Users\YourName\Documents\SpeechProjects
    ```

3.  **Create the virtual environment named "speechrec":**
    ```bash
    python -m venv speechrec
    ```

4.  **Activate the virtual environment:**
    ```bash
    .\speechrec\Scripts\activate
    ```
    You'll notice `(speechrec)` at the beginning of your prompt, indicating that the virtual environment is active.

## 2. Installing Libraries and Testing

Once your virtual environment is active, you can install the required libraries.

1.  **Install the necessary packages:**
    ```bash
    pip install openai-whisper pydub audioop-lts
    ```
    This may take a few moments.

2.  **Test the installation with a sample audio file:**
    Assuming you have a file named `test.mp3` in your current directory (you would need to provide this file yourself), run:
    ```bash
    whisper "./test.mp3" --model base.en
    ```
    This command will use the `openai-whisper` library to transcribe the `test.mp3` file using the `base.en` English model.

## 3. Downloading and Running a Python File from GitHub

You might need to download specific Python scripts from GitHub. Here's how to do it and run them.

1.  **Download a Python file (example):**
    You can typically download a raw file directly from GitHub by navigating to the file on the GitHub website, clicking the "Raw" button, and then saving the page (e.g., right-click and "Save As...") to your desired location.

    For example, if you wanted to download a script from `https://raw.githubusercontent.com/Family-Court-Tools-UK/transcribe-audio/refs/heads/main/whisper_transcribe.py`, you would visit that URL and save the content as `whisper_transcribe.py` in your project directory.

    Or, if you are using Windows Powershell, you could do this:

    `Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Family-Court-Tools-UK/transcribe-audio/refs/heads/main/whisper_transcribe.py" -OutFile "whisper_transcribe.py"`


3.  **Run the downloaded Python file:**
    Make sure you are in the directory where you saved `whisper_transcribe.py` and your `speechrec` virtual environment is active.
    ```bash
    python .\whisper_transcribe.py
    ```
    *Note: The actual execution of a downloaded script will depend on its contents and required arguments. This is a generic example.*

## 4. Checking and Updating Your Python Installation

### How to check if Python is installed:

Open your terminal or command prompt and type:
```bash
python --version
````

If Python is installed, it will display the installed version (e.g., `Python 3.13.3`). If it's not installed or not in your PATH, you'll receive an error message.

### How to download the latest Python using Winget:

If you have an older version of Python or don't have it installed, and you are on Windows 10, you can use Winget (Windows Package Manager) to install the latest version.

1.  **Open PowerShell or Command Prompt as an administrator.** (Right-click on the Start button, then select "Windows Terminal (Admin)" or "Command Prompt (Admin)").

2.  **Run the following command to install Python 3.13.5 (or the specified version):**

    ```bash
    winget install --id=Python.Python.3.13 -v 3.13.5 -e
    ```

    This command tells Winget to install the package with the ID `Python.Python.3.13` and specifically requests version `3.13.5`. The `-e` flag ensures an exact version match.

After installation, close and reopen your terminal for the changes to take effect, and then you can check the Python version again using `python --version`.

