import os
import requests

from dotenv import load_dotenv

def translate(source, target , text): # Translating function
    url = "https://api.sunbird.ai/tasks/nllb_translate"

    language_codes= {
        "English": "eng",
        "Luganda": "lug",
        "Runyankole": "nyn",
        "Acholi": "ach",
        "Ateso": "teo",
        "Lugbara": "lgg"
    }
    sourcecode = language_codes[source]
    targetcode = language_codes[target]
    data = {
        "source_language" : sourcecode,
        "target_language" : targetcode,
        "text" : text
    }
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwYXRyaWNrY21kIiwiYWNjb3VudF90eXBlIjoiRnJlZSIsImV4cCI6NDg2OTE4NjUzOX0.wcFG_GjBSNVZCpP4NPC2xk6Dio8Jdd8vMb8e_rzXOFc"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, json=data)   

    print(response.json()['output']['data']['translated_text'])

def main():
    while(True):
        source = input("Please choose the source language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi):  \nUser:")
        target = input("Please choose the target language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi): \nUser: ")
        userText = input("Enter the text to translate:\nUser: ")
        translate(source, target,userText)
        
        keyClicked = input("Press any key to continue and 0 to exit:\nUser: ")
        if(keyClicked == '0'):
            break

main()
