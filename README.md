**RoboSpeaker**

****Introduction****

RoboSpeaker 1.1 is a simple text-to-speech (TTS) Python application that utilizes Windows PowerShell's built-in speech synthesis feature to convert text input into spoken words. This project was created by Harish and serves as a lightweight speech assistant.

****Features:****

Accepts user input and converts it into speech.

Uses PowerShell's System.Speech.Synthesis for voice output.

Allows exiting the program by entering 'q'.

****Requirements:****

Windows OS (PowerShell must be available)

Python 3.x installed

****How to Run:****

Clone or download this repository.

Open a terminal or command prompt and navigate to the project directory.

Run the script using:

1.python robospeaker.py

Enter text, and the system will speak it aloud.

To exit, type 'q' and press Enter.

****Code Explanation:****

The script continuously prompts the user for input.

If the user enters 'q', the program exits with a farewell message.

Any other input text is spoken using PowerShell's System.Speech.Synthesis.SpeechSynthesizer.

**Example Usage:**

Welcome to RoboSpeaker 1.1 Created by Harish
Enter what you want me to pronounce: Hello, how are you?
(Computer speaks: "Hello, how are you?")
Enter what you want me to pronounce: q
Exiting, Goodbye
(Computer speaks: "Goodbye, friend")

****Future Enhancements:****

Add support for different voices and speech rates.

Implement a graphical user interface (GUI) for better usability.

Extend support to other operating systems.
