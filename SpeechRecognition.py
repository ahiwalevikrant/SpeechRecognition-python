import speech_recognition as sr
import requests

def transcribe_audio_from_url(audio_url):
    # Download the audio file from the URL
    r = requests.get(audio_url)
    
    # Save the audio file locally
    with open("audio_file.mp3", "wb") as f:
        f.write(r.content)

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile("audio_file.mp3") as source:
        audio_data = recognizer.record(source)  # Read the entire audio file

    # Use Google Speech Recognition to transcribe the audio
    try:
        transcription = recognizer.recognize_google(audio_data)
        print("Transcription:", transcription)
    except sr.UnknownValueError:
        print(" Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    audio_url = input("Enter the URL of the MP3 audio file: ")
    transcribe_audio_from_url(audio_url)
