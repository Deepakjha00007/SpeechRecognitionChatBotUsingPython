import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
import importlib
importlib.reload(musicLibrary)




recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="6624a3ed1f1149f09de18d1fc5295eb1"

def speak(text):
    engine.say(text)
    engine.runAndWait()

#     #pip install pygame

# # def speak(text):
# #     tts=gTTS(text)
# #     tts.save("temp.mp3")


# #     pygame.mixer.init()

# #     pygame.mixer.music.load("temp.mp3")

# #     pygame.mixer.music.play()

# #     while pygame.mixer.music.get_busy():
# #         pygame.time.clock().tick(10)

# #     pygame.mixer.music.unload()
# #     os.remove("temp.mp3")
  








def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https//www.instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://in.linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "play" in c.lower():
        song=c.lower().replace("play","").strip()
        if song in musicLibrary.music:
            link=musicLibrary.music[song]
            speak(f"playing {song}")
            webbrowser.open(link)
        else:
            speak("I could'nt fint that song in your library")

    elif "news" in c.lower() :
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apikey=API_KEY")
        if r.status_code == 200:
            data=r.json()

            articles=data.get("articles",[])

            for article in articles:
                speak(article['title'])




if __name__== "__main__":
    speak("initializing jarvis.... ")

    while True:
         #listen for the wake word "jarvis"
         #obtain audio from the microphone
         r=sr.Recognizer()
         

         print("recognizing...")

       #recognize speech using sphinx
         try:
             with sr.Microphone() as source:
                 print("listening !")
                 audio=r.listen(source,timeout=5,phrase_time_limit=3)
             word=r.recognize_google(audio)

             if "jarvis" in word.lower():
                 speak("yeah!")
                 time.sleep(1)
  
                 with sr.Microphone() as source:
                     print("jarvis active !")
                     audio=r.listen(source)
                     command=r.recognize_google(audio)

                     processcommand(command)

                     ("task completed successfully")
            
      
         except Exception as  e:
             print("error;{0}".format(e))


   
