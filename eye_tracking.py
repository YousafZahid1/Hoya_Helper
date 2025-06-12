import cv2
import mediapipe as mp
import pyautogui
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


def jarvis():
    pass

def both():
    eye_tracking()
    jarvis()
import tkinter as tk
import random as r

##### SIGN UP PAGE #####

# Create the Login window
first = tk.Tk()
first.geometry("500x500")
first.title("Computer HELPER")

# Title Label
label = tk.Label(first, text="Computer Helper", font=('Bold', 28))
label.pack(padx=50, pady=30)

##
label = tk.Label(first, text="Your handy dandy helper", font=('Arial', 15))
label.place()



# Labels and Entry fields for username and password


# Function to handle login

# Button for login
button = tk.Button(first, text="Enable JARVIS", font=('Bold', 15))
button.pack(pady=20)

button = tk.Button(first, text="Enable Eye Tracker", font=('Bold', 15),command=eye_tracking)
button.pack(pady=40)


button2 = tk.Button(first,text="Enable Eye Tracker & Enable JARVIS", font=('Bold', 15),command=both)
button2.pack(pady=30)
# Run the Login window

first.mainloop()

