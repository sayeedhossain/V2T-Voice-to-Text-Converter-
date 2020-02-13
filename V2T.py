import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please Speak Anything Which You Want:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("Sir You Said : {}".format(text))
    except:
        print("Sorry sir, could not recognize what you said")
