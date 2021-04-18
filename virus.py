import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import time


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

      elif 'linkedin' in query:
          webbrowser.open("https:\\www.linkedin.com\\feed\\")
                     

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
         
          

      elif 'visual' in query:
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

      
      elif 'game' in query :
          print("Stone Paper Scissors: VIRUS")
          time.sleep(1.0)
          print('You have 10 Chances')
          time.sleep(1.0)
          print('Start')
          time.sleep(2.0)


          level = 11
          onLevel = 0
          score = 0
          opponentScore = 0
          while level >= 1 :
              level = level - 1
              onLevel = onLevel + 1
              if level == 0 and score == opponentScore:
                  print("Result: Tie")


              elif level == 0 and score > opponentScore:
                  print("Result: You win")


              elif level == 0 and score < opponentScore:
                  print("Result: You loose")


              else:
                   randChoice = ["STONE", "PAPER", "SCISSOR"]
                   opponentChoice = random.choice(randChoice)
                   print("Level: " + str(onLevel))
                   yourChoice = input('Choose STONE  PAPER or SCISSOR: ')
                   yourChoice = yourChoice.upper()

                   if yourChoice == opponentChoice:
                      print("Your Choice: {0} Opponent Choice: {1}".format(yourChoice, opponentChoice))
                      print("Your Score: " + str(score) + " || Opponent Score: " + str(opponentScore) + "\n")

                   elif yourChoice == "STONE" and opponentChoice == "SCISSOR":
                      score += 1
                      print("Your Choice: {0} Opponent Choice: {1}".format(yourChoice, opponentChoice))
                      print("Your Score: {0} || Opponent Score: {1}\n".format(str(score), str(opponentScore)))
                    

                   elif yourChoice == "PAPER" and opponentChoice == "STONE":
                      score += 1
                      print("Your Choice: {0} Opponent Choice: {1}".format(yourChoice, opponentChoice))
                      print("Your Score: {0} || Opponent Score: {1}\n".format(str(score), str(opponentScore)))

                   elif yourChoice == "SCISSOR" and opponentChoice == "PAPER":
                      score += 1
                      print("Your Choice: {0} Opponent Choice: {1}".format(yourChoice, opponentChoice))
                      print("Your Score: {0} || Opponent Score: {1}\n".format(str(score), str(opponentScore)))

                   elif yourChoice not in randChoice:
                      print("Invalid input")

                   else:
                      opponentScore += 1
                      print("Your Choice: {0} Opponent Choice: {1}".format(yourChoice, opponentChoice))
                      print("Your Score: {0} || Opponent Score: {1}\n".format(str(score), str(opponentScore)))
    
      elif 'source' in query:
          speak("link in description")

         
      





