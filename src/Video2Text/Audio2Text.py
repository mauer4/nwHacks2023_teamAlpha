import requests
import json

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
headers = {"Authorization": "Bearer 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"}

def audio2text(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    response = json.loads(response.content.decode("utf-8"))
    
    # String to write to the file
    response_text = response['text']
    
    # Open the file in write mode
    with open("speech.txt", "w") as file:
        file.write(response_text)
