#Akhbaar padhke sunaao
import requests
from win32com.client import Dispatch
speak=Dispatch("SAPI.SpVoice")
speak.Speak("Welcome to News application")
r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=732f121d0b66458bac3fb5bf326db1e3")
data=r.json()["articles"]
def NewsSpeak(str):
    speak.Speak(str)
speak.Speak("Here are some news Headlines")
for i in data:
    toRead=f"{data.index(i)+1} {i['title']}"
    print(toRead)
    speak.Speak(toRead)

