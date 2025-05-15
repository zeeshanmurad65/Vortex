import speech_recognition as sr
import webbrowser
import pyttsx3
from gtts import gTTS
import requests  
import pocketsphinx
import Favorite_musics
import pygame
import time
import os
recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="your api"
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
   tts = gTTS(text)
   tts.save('hello.mp3')
  
   pygame.mixer.init()

# Load and play the MP3 file
   pygame.mixer.music.load("hello.mp3")
   pygame.mixer.music.play()

# Keep the program running while music plays
   while pygame.mixer.music.get_busy():
     pygame.time.Clock().tick(10)    
   pygame.mixer.music.unload()
   os.remove("hello.mp3")
   #  For AI integeration in my projects
def deepseek(prompts):
    headers = {
        'Authorization': 'sk-1cc0fbd76dbb47f08442c0b2d53abdf3asss',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompts}]
    }
    response = requests.post('https://api.deepseek.com/v1/chat/completions', 
                           headers=headers, json=data)
    return response.json()
#  All code are performing here for function
def processcomand(c):
   if "open google" in c.lower():
      speak("Google is Opening")
      webbrowser.open("https://google.com")
   elif "open youtube" in   c.lower():
      webbrowser.open("https://youtube.com")
      speak("Youtube is Opening")
   elif "open facebook" in   c.lower():
      webbrowser.open("http://facebook.com")
      speak("Facebook is Opening")
   elif "open tiktok" in c.lower():
        webbrowser.open("http://tiktok.com")
        speak("Tiktok is Opening")
   elif c.lower().startswith("play"):
      song=c.split(" ")[1]  
      link=Favorite_musics.music[song] 
      webbrowser.open(link)
      speak(f"{c} is Opening")
   elif "news" in c.lower():
      r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
      if r.status_code== 200:
        data = r.json()
# Extract and display headlines
        articles = data.get("articles", [])
        for article in articles:
         speak(article['title'])
   else:
       output=deepseek(c)
       speak(output)         
if __name__=="__main__" :
 while(True):
    speak("Activating Vortex...")
    # Listen for Word Vortex
    # obtain audio from Microphone
    r=sr.Recognizer()
    print(" Intializing Vortex ....")
    try:
        with sr.Microphone() as source:
          print(" Listening...")
          audio=r.listen(source,timeout=2, phrase_time_limit=1)
          name=r.recognize_google(audio)
          if("vortex" == name.lower()):
            print("Yes! Zeeshan")
            with sr.Microphone() as source:
              speak("What can I do for You ?")
              audio=r.listen(source)
              command=r.recognize_google(audio)
              processcomand(command)
    except Exception as e:
      print("!Sorry didn't Understand you.")  
    