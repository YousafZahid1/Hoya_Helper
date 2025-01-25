import speech_recognition as sr
import website_open as wo  # Assuming website_opener is inside this module

def detect_voice():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    counter = 0

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for commands...")

        while True:  # Continuous loop to listen for commands
            try:
                print("Listening...")
                audio = recognizer.listen(source)  # Capture the audio

                # Use Google's speech recognition engine
                text = recognizer.recognize_google(audio).lower()
                print(f"Detected voice input: {text}")

                # Check for commands
                if 'hello' in text:
                    print("Hello! How can I assist you?")
                elif 'open' in text:
                    # Extract the website name after 'open'
                    if text == 'open':
                        continue
                    site = text.split('open ')[-1].strip()
                    if site:
                        print(f"Opening {site}...")
                        wo.website_opener(site)  # Use the website opener function
                    else:
                        print("Sorry, I couldn't understand the website name.")
                elif 'exit' in text:
                    print("Goodbye!")
                    break  # Exit the loop and stop the program
                else:
                    counter = counter + 1
                    print("Unkown command.")
                    recognizer.adjust_for_ambient_noise(source, duration=.1)
                    
                    if counter > 5:
                        print ("Too many errors, quitting.")
                        break

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Sorry, there was an error with the speech recognition service.")
            except Exception as e:
                print(f"An error occurred: {e}")
