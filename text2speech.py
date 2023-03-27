
from google.cloud import texttospeech
from google.oauth2 import service_account
import pygame
import time


def speech(content):
    print(content)
    # Create a credential object from your service account file
    credentials = service_account.Credentials.from_service_account_file(
        "/home/asl/.config/Google/gcloud/service_admin.json")

    # Pass the credentials to the client constructor
    client = texttospeech.TextToSpeechClient(credentials=credentials)

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=content)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="ro", name="",
    )


    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        pitch=0,

    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("outputAI.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "outputAI.mp3"')

    pygame.mixer.init()

    sound = pygame.mixer.Sound('outputAI.mp3')
    sound.play()
    time.sleep(sound.get_length())
