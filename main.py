import cv2
import mediapipe as mp
import pyautogui
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
               audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)  # Capture the audio with reduced timeout and phrase_time_limit


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




def eye_tracking():
    sensitivity = 1.2 # varaible here for
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w * landmark.x * sensitivity
                    screen_y = screen_h * landmark.y * sensitivity
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            print(left[0].y-left[1].y)
            
            if (left[0].y - left[1].y) < 0.013: # change back to 0.004
                pyautogui.click()
                pyautogui.sleep(1)
        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)




def both():
    eye_tracking()
    detect_voice()
import tkinter as tk
import random as r

##### SIGN UP PAGE #####

# Create the Login window
first = tk.Tk()
first.geometry("500x500")
first.title("Computer HELPER")

# Title Label
label = tk.Label(first, text="Hoya Helper", font=('Bold', 28))
label.pack(padx=50, pady=30)

##
label = tk.Label(first, text="Your handy dandy helper", font=('Arial', 15))
label.place()


##

# Labels and Entry fields for username and password


# Function to handle login

# Button for login
button = tk.Button(first, text="Enable JARVIS", font=('Bold', 15),command=detect_voice)
button.pack(pady=20)

button = tk.Button(first, text="Enable Eye Tracker", font=('Bold', 15),command=eye_tracking)
button.pack(pady=40)


button2 = tk.Button(first,text="Enable Eye Tracker & Enable JARVIS", font=('Bold', 15),command=both)
button2.pack(pady=30)
# Run the Login window





first.mainloop()

