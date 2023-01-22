import requests

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

output = query("videospeech.flac")