
import speech_recognition as sr 
import pyttsx3 
import datetime
import wikipedia
r = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
o = "Hi There, How can I help You"
print(o)

with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source,timeout = 5)

try:
      command = r.recognize_google(audio)
      print(command)
      if "time" in command:
        t =  datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {t}") 
        print(f"The time is {t}")    
      elif "stop" in command:
        speak("goodbye")
      elif "date" in command:
          d =  datetime.date.today().strftime("%B %d, %Y")
          print(f"today is {d}") 
          speak(f"today is {d}") 
      else:
          re = wikipedia.summary(command,sentences = 3)
          print(re)
          speak(re)

except:
    print("error")
    speak("error")
 
    






