import pyttsx3
AI = pyttsx3.init()
print("What should the AI Bot say")
a = input(">")
AI.say(a)
AI.runAndWait()
