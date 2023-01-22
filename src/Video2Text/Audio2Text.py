import requests
import time
import json

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
headers = {"Authorization": "Bearer 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"}

def audio2text(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    while 'error' in response:
        if(response['error'] == "Model openai/whisper-base is currently loading"):
            print("Still loading: trying again in 20 seconds.")
            time.sleep(10)
        else:
            print("Uknown error - abort app")
            break
    response = json.loads(response.content.decode("utf-8"))
    
    # String to write to the file
    response_text = response['text']
    
    # Open the file in write mode
    with open("speech.txt", "w") as file:
        file.write(response_text)
