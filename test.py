import speech_recognition as sr
import webbrowser

# Function to open websites
def open_website(command):
    websites = {
        "youtube": "https://www.youtube.com",
        "amazon": "https://www.amazon.com",
        "google": "https://www.google.com",
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
    }

    for keyword, url in websites.items():
        if keyword in command:
            print(f"Opening {keyword}...")
            webbrowser.open(url)
            return
    print("Sorry, I couldn't understand the command. Try again!")

# Function to listen to user commands
def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Sorry, there's an issue with the speech recognition service.")
        except Exception as e:
            print(f"An error occurred: {e}")
    return ""

# Main program loop
if __name__ == "__main__":
    print("Voice Command Program is ready. Say a command like 'open YouTube' or 'open Amazon'.")
    while True:
        command = listen_for_command()
        if command:
            if "exit" in command or "quit" in command:
                print("Exiting program. Goodbye!")
                break
            open_website(command)
