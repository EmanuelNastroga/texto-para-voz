import pyttsx3 as pyttsx3
engine = pyttsx3.init()

def setRate(r):
    """ RATE"""
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    engine.setProperty('rate', r)  # setting up new voice rate
def setVolume(v):
    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    engine.setProperty('volume', v)  # setting up volume level  between 0 and 1
def setVoice(t):
    """VOICE"""
    voices = engine.getProperty('voices')  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[t].id)  # changing index, changes voices. 1 for female

def SpeakText(command):
    #engine = pyttsx3.init()

    engine.say(command)
    engine.runAndWait()


#SpeakText("hérika meu amor")