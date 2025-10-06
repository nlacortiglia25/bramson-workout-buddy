import subprocess
import platform

# Exception thrown if 60 seconds passes with nothing added to the speach queue
def text_to_speech(queue):

    print("\ttts thread started.")
    system = platform.system()

    while(True):
        print("\ttts waiting for item...")
        message = queue.get(block = True, timeout=60)
        print(f"\tqueue has about {queue.qsize()} items")
        print(f"\ttts speaking this message: {message}...")
        
        match system:
            case "Windows":
                subprocess.run(["powershell", "-Command", f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message}')"])
            case "Linux":
                subprocess.run(["espeak", message])
            case "Darwin":
                subprocess.run(["say", message])

        print(f"\tfinished speaking...")