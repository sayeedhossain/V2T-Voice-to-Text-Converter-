This repository contains resources from The Ultimate Guide to Speech Recognition with Python tutorial on Real Python.

Audio files for the examples in the Working With Audio Files section of the post can be found in the audio_files directory. To download them, use the green "Clone or download" button at the top right corner of this page.

The guessing_game.py file contains the full source code for the "Guess a Word" game example.

NOTE: You will need to install the SpeechRecognition and PyAudio packages in order to run the example. Please see the tutorial for step-by-step instructions.

You can test your SpeechRecognition and PyAudio installation by downloading guessing_game.py and typing the following into a Python REPL session:

>>> import speech_recognition as sr
>>> from guessing_game.py import recognize_speech_from_mic
>>> r = sr.Recognizer()
>>> m = sr.Microphone()
>>> recognize_speech_from_mic(r, m)  # speak after running this line
{'success': True, 'error': None, 'transcription': 'hello'}
Of course, your output will vary depending on what you said after running recognize_speech_from_mic(r, m).


<h4>Any further query? just feel free to contact at (me@sayeedhossain.com) </h4>

