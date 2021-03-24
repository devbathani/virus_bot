import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING DEV")

    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON DEV")

    else:
        speak("GOOD EVENING DEV")


    speak("hiii Dev. What you want me to do")               

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")


    except Exception as e:
        #print(e)
        print("SORRY BRO CAN YOU REPEAT PLEASE..") 
        return "None"
    return query

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bathanid888@gmail.com', 'bathanidev888')
    server.sendmail('bathanid888@gmail.com', to , content)
    server.close()

   
if __name__ == "__main__":
   wishMe()
   while True:
   #if 1:
      query = takeCommand().lower()

      if 'wikipedia' in query:
         speak('SEARCHING WIKIPEDIA...')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak("ACCORDING TO WIKIPEDIA")
         print(results)
         speak(results)

      elif 'youtube' in query:
           webbrowser.open("youtube.com")

      elif 'google' in query:
           webbrowser.open("google.com")

      elif 'amazon prime' in query:
           webbrowser.open("primevideo.com")

      elif 'netflix' in query:
          webbrowser.open("netflix.com")     

      elif 'classroom' in query:
           webbrowser.open("classroom.google.com")     

      elif 'stock' in query:
           webbrowser.open("in.tradingview.com")    

      elif 'gmail' in query:
           webbrowser.open("https:\\mail.google.com\\mail\\u\\0\\#inbox")        

      elif 'instagram' in query:
          webbrowser.open("instagram.com")      

      elif 'whatsapp' in query:
           webbrowser.open("web.whatsapp.com")          

      elif 'play' in query:
          music_dir = 'D:\\dj songs'
          songs = os.listdir(music_dir)
          s_list = random.choice(songs)   
          print(songs)
          os.startfile(os.path.join(music_dir, s_list))

      elif 'time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"bro its {strTime}")
          print("TIME : ", strTime)    

      elif 'code' in query:
          codePath = "C:\\Users\\batha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
          os.startfile(codePath)

      elif 'steam' in query:
          path = "C:\\Program Files (x86)\\Steam\\steam.exe"
          os.startfile(path)    

      elif 'unity' in query:
          unitypath = "C:\\Program Files\\Unity Hub\\Unity Hub.exe"
          os.startfile(unitypath)    

      elif 'dj' in query:
          djpath = "C:\\Program Files\\VirtualDJ\\virtualdj.exe"
          os.startfile(djpath)        

      elif 'studio' in query:
          studioPath = "C:\\Program Files\\Android\\Android Studio1\\bin\studio64.exe"    
          os.startfile(studioPath)

      elif 'hi' in query:
          speak("kasa hai tu bro")    

      elif 'mail' in query:
          try:
              speak("what should i say?")
              content = takeCommand()
              to = "bathanidev888@gmail.com"
              sendMail(to, content)
              speak("hogaya bro")
          except Exception as e:
              print(e)
              speak("bro nahi hua")      

      elif 'how are you' in query:
          speak("m good. how are u bro")    

      elif 'good' in query:
          speak("so tell me how was your day ?") 
          speak("what would you like to do ?")      
   
      elif 'bhai' in query:
          speak("ok !  LOVE YOU")       

        






