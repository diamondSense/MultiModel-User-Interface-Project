# MultiModel-User-Interface-Project Spring 2025 UNIFR
##  Interactive Cooking Assitance 
“Enhancing Cooking Experiences with Multimodal Interaction”
The goal of this project is to have interactive cooking assistant that responds to voice and object recognition.

## Environment
To create the environment you can use the following command:

```bash
python -m venv .venv
```

Then you can activate the environment with the following command:

```bash
source .venv/bin/activate
```

use this requirements.txt file to load the necessary packages:

```bash
pip freeze > requirements.txt
```

## Technology
Voice Recognition - Google Speech to text / Whisper

Install speech to text client library 

```bash
pip install --upgrade google-cloud-speech
```

To use Whisper take a look at quickstart here https://platform.openai.com/docs/guides/speech-to-text

Object Recognition - MediaPipe + OpenCV

To install MediaPipe:

```bash
pip install mediapipe
```

To install OpenCV

```bash
pip install opencv-python
```

User Interface - AR overlays(OpenCV) or simple web UI
