import os
# import logging
# logging.basicConfig(level=logging.CRITICAL)  # Suppress logging issues

# import pyttsx3
# engine = pyttsx3.init()



if __name__ == '__main__':

    print("Welcome to RoboSpeaker 1.1 Created bu Harish")
   
    while True:    
      x = input("Enter what you want me to pronounce: ")
      
      if x.lower() == "q":
        print("Exiting , Goodbye")
        os.system("powershell -c \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Goodbye, friend')\"")
        # engine.stop()
        # engine = None
        break
    # text = input("Enter what you want me to pronounce: ")
    # engine.say(x)
    # engine.runAndWait()
      command = f"powershell -c \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')\""
      os.system(command)