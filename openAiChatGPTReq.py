import openai
import requests
import json
import record
import whisperApi
import text2speech
from dotenv import load_dotenv
import os

load_dotenv()

while True:
    record.record()
    message = whisperApi.whisperapi()
    print(message)
    with open('log.txt', 'r') as f:
        lines = f.read()
        messages = lines + '\n' + message
        print(message)

    apiKey = os.getenv("API_KEY")
    openai.api_key = apiKey

    headers = {"Authorization": f"Bearer {apiKey}",
               "content-type": "application/json"}

    data = {'model': 'gpt-4-32k-0613',
           "messages": [{"role": "user", "content": messages}],

           'temperature': 0.1

        ,
           'max_tokens': 250
            }


    jsonData = json.dumps(data)

    req = requests.post(
        url="https://api.openai.com/v1/chat/completions",
        headers=headers,
        data = jsonData,

    )
    binaryJSON = req.content
    decodedJsonData = json.loads(binaryJSON.decode())



    content = decodedJsonData["choices"][0]["message"]["content"]

    text2speech.speech(content)

    with open('log.txt', "w") as f:
        f.write(f'Human: {message}\n')
        f.write(f'AI: {content}\n')
        f.close()

