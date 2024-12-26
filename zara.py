import sqlite3
import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import datetime 
import wikipedia
import webbrowser
import pywhatkit as wk
import cv2
import random
import operator
import requests
import sys
import pyautogui
import time
import os
import tkinter as tk 
from tkinter import messagebox
import threading
import math


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(audio):                             
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good Evening!")

    speak("Ready To Comply. What can I do for you ?")            

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language= 'en-in',)
            print(f"User said: {query}\n")

        except Exception as e:
            print("say that again please...")
            speak("say that again please...")
            return "None"
        return query
    


import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('voice_assistant.db')
cursor = conn.cursor()

# Create users table with phone number instead of email
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
)
''')

# Create voice_commands table
cursor.execute('''
CREATE TABLE IF NOT EXISTS voice_commands (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    command TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
''')

# Insert data into users table
cursor.execute('''
INSERT INTO users (name, phone) 
VALUES ('Alice', '123-456-7890')
''')
cursor.execute('''
INSERT INTO users (name, phone) 
VALUES ('Bob', '098-765-4321')
''')

# Insert data into voice_commands table
cursor.execute('''
INSERT INTO voice_commands (user_id, command) 
VALUES (1, 'Play music')
''')
cursor.execute('''
INSERT INTO voice_commands (user_id, command) 
VALUES (2, 'Set an alarm for 7 AM')
''')

# Commit the changes
conn.commit()

# Query users table
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()

print("Users:")
for user in users:
    print(user)

# Query voice_commands table
cursor.execute('SELECT * FROM voice_commands')
commands = cursor.fetchall()

print("\nVoice Commands:")
for command in commands:
    print(command)

# Close the connection
conn.close()


if __name__ == "__main__":
    def run_voice_assistant():

        wishMe()
        while True:
            query = takeCommand().lower()

            if 'zara' in query:
                 print("yes sir")
                 speak("yes sir")
        
            elif 'type' in query: #10
                 query = query.replace("type","")
                 pyautogui.typewrite(f"{query}",0.1)
                 pyautogui.press('enter')

            elif "who are you" in query:
                 print('My Name Is Zara')
                 speak('My Name Is Zara')
                 print('I can Do Everything that my creator Programmed me to do')
                 speak('I can Do Everything that my creator Programmed me to do')

            elif "who created you" in query:
                 speak('I Don not Know His Name, I created with python Language, in Visual Studio code.')
                 print('I Don not Know His Name, I created with python Language, in Visual Studio code.') 

            elif "thank you" in query:
                 print('You are Welcome')
                 speak('You are Welcome') 


            elif 'what is the' in query:
                  speak('Searching Wikipedia...')
                  query = query.replace("what is","")
                  results = wikipedia.summary(query, sentences=2)
                  speak("According to wikipedia")
                  print(results)
                  speak(results)

            elif 'who is the' in query:
                 speak('Searching Wikipedia...')
                 query = query.replace("who is","")
                 results = wikipedia.summary(query, sentences=2)
                 speak("According to wikipedia")
                 print(results)
                 speak(results)    

            elif 'just open google' in query:    
                  webbrowser.open('google.com')

            elif 'open google' in query:
                  speak("what should I search ?")
                  qry = takeCommand().lower()
                  webbrowser.open(f"{qry}")
                  results = wikipedia.summary(qry, sentences=1)
                  speak(results)

            elif  'just open youtube' in query:
                 
                  webbrowser.open('youtube.com')

            elif 'open youtube' in query:
                  speak("what you will like to watch ?")
                  qrry = takeCommand().lower()
                  wk.playonyt(f"{qrry}")
 
            elif 'search on youtube' in query:
                 query = query.replace("search on youtube","")
                 webbrowser.open(f"www.youtube.com/results?search_query={query}")

            elif 'close browser' in query:
                 os.system("taskkill /f /im msedge.exe")        

            elif 'close chrome' in query:
                 os.system("taskkill /f /im chrome.exe")

            elif "open paint" in query: #13
                 npath = "C:\paint"
                 os.startfile("npath")

            elif "draw a line" in query:
                   pyautogui.moveTo(x=400, y=300, duration=1)
                   pyautogui.leftClick
                   pyautogui.dragrel(400, 0, 1)

            elif "close paint" in query:
                  os.system("taskkill /f /im mspaint.exe")
        
            elif "open notepad" in query:
                  npath = "c:\WINDOWS\system32\\notepad.exe"    
                  os.startfile(npath)

            elif "close notepad" in query:
                      os.system("taskkill /f /im notepad.exe")

            elif "open command prompt" in query:
                  os.system("start cmd")

            elif "close command prompt" in query:
                   os.system("taskkill /f /im cmd.exe")
          
            elif 'tell me the time' in query:
                  strTime = datetime.datetime.now().strftime("%H:%M:%S")
                  speak(f"sir, the time is {strTime}")

            elif "shutdown the system" in query:
                 os.system("shutdown /s /t 5")
                 time.sleep(1)
                 pyautogui.press("close")

            elif "restart the system" in query:
                  os.system("shutdown /r /t 5")

            elif "lock the system" in query:
             os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "hibernate the system" in query:
                  os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")   

            elif  "open camera" in query:
                 cap = cv2.VideoCapture(0)
                 while True:
                     ret, img = cap.read()
                     cv2.imshow('webcam', img)
                     k = cv2.waitKey(50)
                     if k==27:
                        break;
                 cap.release()
                 cv2.destroyAllWindows()

            elif "go to sleep" in query:
                 speak('alright then, I am switching off')
                 sys.exit()

            elif "take screenshot" in query:
                   speak('tell me a name for the file')
                   name = takeCommand().lower()
                   time.sleep(3)
                   img = pyautogui.screenshot()
                   img.save(f"{name}.png")
                   speak("screenshot saved")

            elif "calculate" in query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                     speak("ready")
                     print("listening...")
                     r.adjust_for_ambient_noise(source)
                     audio = r.listen(source)
                     my_string = r.recognize_google(audio)
                     print(my_string)    
                     def get_operator_fn(op):
                      return{
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' : operator.__truediv__,
                        }[op]   
                     def eval_binary_expr(op1,oper, op2):
                         op1,op2 = int(op1), int(op2)
                         return get_operator_fn(oper)(op1, op2)
                     speak("your result is")
                     speak(eval_binary_expr(*(my_string.split())))

            elif "what is my ip address" in query:
                 speak("checking")
                 try:
                     ipAdd = requests.get('https://api.ipify.org').text
                     print(ipAdd)
                     speak("your ip address is") 
                     speak(ipAdd)         
                 except Exception as e:
                    speak("network is weak,please try again some time later")
                   
            elif "volume up" in query:
                 pyautogui.press("volumeup")
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup") 
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup")  
                 pyautogui.press("volumeup")  

            elif "volume down" in  query:
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
                 pyautogui.press("volumedown")
 
            elif "mute" in query:
                 pyautogui.press("volumemute")     

            elif "unmute" in query:
                 pyautogui.press("volumemute")                
        
            elif "hello" in query:
                  speak("hello ,sir")
                  print("hello ,sir")

            elif "how are you" in query:
                 speak("I am fine ,what about you")
                 print("I am fine ,what about you")

            elif "i am fine" in query:
                 speak("well ,I'm glad to hear it")
                 print("well ,I'm glad to hear it")       

            elif 'open chrome' in query:
                 os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')

            elif 'maximize this window' in query:
                 pyautogui.hotkey('alt', 'space')
                 time.sleep(1)
                 pyautogui.press('x')

            elif 'google search' in query:
                 query = query.replace("google search", "")
                 pyautogui.hotkey('alt', 'd')
                 pyautogui.write(f"{query}",0.1)
                 pyautogui.press('enter')


            elif 'youtube search' in query:
                 query = query.replace("youTube search","")
                 pyautogui.hotkey('alt', 'd')
                 time.sleep(1)
                 pyautogui.press('tab')    
                 pyautogui.press('tab')
                 pyautogui.press('tab')  
                 pyautogui.press('tab')
                 pyautogui.press('tab')    
                 pyautogui.press('tab')
                 pyautogui.press('tab')  
                 pyautogui.press('tab') 
                 time.sleep(1)
                 pyautogui.write(f"{query}",0.1)
                 pyautogui.press('enter')

            elif 'open new window' in query:
                 pyautogui.hotkey('ctrl', 'n')

            elif 'open incognito window' in query:
                 pyautogui.hotkey('ctrl', 'shift', 'n')

            elif 'minimise this window' in query:
                 pyautogui.hotkey('alt', 'space')
                 time.sleep(1)
                 pyautogui.press('n')

            elif 'open history' in query:
                  pyautogui.hotkey('ctrl', 'h')

            elif 'open downloads' in query:
                 pyautogui.hotkey('ctrl', 'j')

            elif 'previous tab' in query:
                 pyautogui.hotkey('ctrl', 'shift', 'tab')

            elif 'next tab' in query:
                 pyautogui.hotkey('ctrl', 'tab')

            elif 'close tab' in query:
                 pyautogui.hotkey('ctrl', 'w')

            elif 'close window' in query:
                 pyautogui.hotkey('ctrl','shift', 'w')

            elif 'clear browsing history' in query:
                 pyautogui.hotkey('ctrl', 'shift', 'delete')

            elif 'close chrome' in query:
                  os.system("taskkill /f /im chrome.exe")


class ZaraApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zara - Voice Assistant")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Zara Voice Assistant", font=("Arial", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self, text="Start Voice Assistant", command=self.start_voice_assistant)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self, text="Stop Voice Assistant", command=self.stop_voice_assistant)
        self.stop_button.pack(pady=10)

    def start_voice_assistant(self):
        self.voice_thread = threading.Thread(target=run_voice_assistant)
        self.voice_thread.start()

    def stop_voice_assistant(self):
        if self.voice_thread.is_alive():
            sys.exit()

if __name__ == "__main__":
    app = ZaraApp()
    app.mainloop()
