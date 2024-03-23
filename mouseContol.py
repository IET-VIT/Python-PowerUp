# pip install mediapipe==0.9.3.0
# pip install opencv-python numpy
# protobuf 3.20.0


# STEPS:


# Step 1
# import cv2
#
# cap=cv2.VideoCapture(1)
# while True:
#     ret, frame=cap.read()
#     cv2.imshow('Virtual Camera', frame)
#     cv2.waitKey(1)

##################################################################################

# Step 2
# import cv2
# import mediapipe as mp
#
#
# cap=cv2.VideoCapture(1)
# hand_detector=mp.solutions.hands.Hands()
# while True:
#     ret, frame=cap.read()
#     rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output=hand_detector.process(rgb_frame)
#     hands=output.multi_hand_landmarks
#     print(hands)
#     cv2.imshow('Virtual Camera', frame)
#     cv2.waitKey(1)


##################################################################################


# step 3
# import cv2
# import mediapipe as mp
#
#
# cap=cv2.VideoCapture(1)
# hand_detector=mp.solutions.hands.Hands()
# drawing_utils=mp.solutions.drawing_utils
# while True:
#     ret, frame=cap.read()
#     rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output=hand_detector.process(rgb_frame)
#     hands=output.multi_hand_landmarks
#     # print(hands)
#     if hands:
#         for hand in hands:
#             drawing_utils.draw_landmarks(frame, hand)
#     cv2.imshow('Virtual Camera', frame)
#     cv2.waitKey(1)


##################################################################################



# Step 4
#
# import cv2
# import mediapipe as mp
#
#
# cap=cv2.VideoCapture(1)
# hand_detector=mp.solutions.hands.Hands()
# drawing_utils=mp.solutions.drawing_utils
# while True:
#     ret, frame=cap.read()


#     frame=cv2.flip(frame, 1) #0 means flip on x and 1 means flip on y


#     rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output=hand_detector.process(rgb_frame)
#     hands=output.multi_hand_landmarks
#     # print(hands)
#     if hands:
#         for hand in hands:
#             drawing_utils.draw_landmarks(frame, hand)
#             landmarks=hand.landmark
#             # print(landmarks)
#             for id, landmark in enumerate(landmarks):
#                 # print(landmark)
#                 x=landmark.x
#                 # print(x)
#                 y=landmark.y
#                 # print(x, y)
#
#     cv2.imshow('Virtual Camera', frame)
#     cv2.waitKey(1)


##################################################################################

# Step 5
# import cv2
# import mediapipe as mp
#
#
# cap=cv2.VideoCapture(1)
# hand_detector=mp.solutions.hands.Hands()
# drawing_utils=mp.solutions.drawing_utils
# while True:
#     ret, frame=cap.read()
#     frame=cv2.flip(frame, 1) #0 means flip on x and 1 means flip on y
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output=hand_detector.process(rgb_frame)
#     hands=output.multi_hand_landmarks
#     # print(hands)
#     if hands:
#         for hand in hands:
#             drawing_utils.draw_landmarks(frame, hand)
#             landmarks=hand.landmark
#             # print(landmarks)
#             for id, landmark in enumerate(landmarks):
#                 # print(landmark)
#                 x=int(landmark.x * frame_width)
#                 # print(x)
#                 y=int(landmark.y * frame_height)
#                 # print(x, y)
#                 if id==8:
#                     cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255,255))
#     cv2.imshow('Virtual Camera', frame)
#     cv2.waitKey(1)


##################################################################################



# Step4
# import cv2
# import mediapipe as mp
# import pyautogui
#
# cap=cv2.VideoCapture(1)
# hand_detector=mp.solutions.hands.Hands()
# drawing_utils=mp.solutions.drawing_utils
# while True:
#     ret, frame=cap.read()
#     frame=cv2.flip(frame, 1) #0 means flip on x and 1 means flip on y
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output=hand_detector.process(rgb_frame)
#     hands=output.multi_hand_landmarks
#     # print(hands)
#     if hands:
#         for hand in hands:
#             drawing_utils.draw_landmarks(frame, hand)
#             landmarks=hand.landmark
#             # print(landmarks)
#             for id, landmark in enumerate(landmarks):
#                 # print(landmark)
#                 x=int(landmark.x * frame_width)
#                 # print(x)
#                 y=int(landmark.y * frame_height)
#                 # print(x, y)
#                 if id==8:
#                     cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255,255))
#                     pyautogui.moveTo(x,y) # it will move only with your finger cant move to the entire screen
#     cv2.imshow('Virtual Camera', frame)
#     cv2.waitKey(1)


##################################################################################



# Step 5
# import cv2
# import mediapipe as mp
# import pyautogui
#
# cap=cv2.VideoCapture(1)
# hand_detector=mp.solutions.hands.Hands()
# drawing_utils=mp.solutions.drawing_utils
#
#
# screen_width, screen_height=pyautogui.size()
#
#
# while True:
#     ret, frame=cap.read()
#     frame=cv2.flip(frame, 1) #0 means flip on x and 1 means flip on y
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output=hand_detector.process(rgb_frame)
#     hands=output.multi_hand_landmarks
#     # print(hands)
#     if hands:
#         for hand in hands:
#             drawing_utils.draw_landmarks(frame, hand)
#             landmarks=hand.landmark
#             # print(landmarks)
#             for id, landmark in enumerate(landmarks):
#                 # print(landmark)
#                 x=int(landmark.x * frame_width)
#                 # print(x)
#                 y=int(landmark.y * frame_height)
#                 # print(x, y)
#                 if id==8:
#                     cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255,255))
#
#                     index_x=screen_width/frame_width*x
#                     index_y=screen_height/frame_height*y
#
#                     pyautogui.moveTo(index_x,index_y) # it will move only with your finger cant move to the entire screen
#     cv2.imshow('Virtual Camera', frame)
#     cv2.waitKey(1)



##################################################################################





# Step 6
# import cv2
# import mediapipe as mp
# import pyautogui
#
# cap=cv2.VideoCapture(0)
# hand_detector=mp.solutions.hands.Hands()
# drawing_utils=mp.solutions.drawing_utils
# screen_width, screen_height=pyautogui.size()
#
#
# index_y=0
#
# while True:
#     ret, frame=cap.read()
#     frame=cv2.flip(frame, 1) #0 means flip on x and 1 means flip on y
#     frame_height, frame_width, _ = frame.shape
#     rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output=hand_detector.process(rgb_frame)
#     hands=output.multi_hand_landmarks
#     # print(hands)
#     if hands:
#         for hand in hands:
#             drawing_utils.draw_landmarks(frame, hand)
#             landmarks=hand.landmark
#             # print(landmarks)
#             for id, landmark in enumerate(landmarks):
#                 # print(landmark)
#                 x=int(landmark.x * frame_width)
#                 # print(x)
#                 y=int(landmark.y * frame_height)
#                 # print(x, y)
#                 if id==8:
#                     cv2.circle(img=frame, center=(x,y), radius=15, color=(0, 255,255))
#                     index_x=screen_width/frame_width*x
#                     index_y=screen_height/frame_height*y
#                     pyautogui.moveTo(index_x,index_y) # it will move only with your finger cant move to the entire screen
#                 if id==4:
#                     cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
#                     thumb_x = screen_width / frame_width * x
#                     thumb_y = screen_height / frame_height * y
#
#                     if abs(index_y-thumb_y)<30:
#                         print('click')
#                         pyautogui.click()
#                         pyautogui.sleep(1)
#     cv2.imshow('Virtual Camera', frame)
#     cv2.waitKey(1)








# Final
import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(1)  # Adjust the camera index if necessary
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height=pyautogui.size()
index_y=0

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error reading frame from camera")
        continue

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        print("Detected hands:", len(hands))
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            # print("Number of landmarks:", len(landmarks))
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                # print("Landmark", id, ":", x, y)

                if id == 8:
                    cv2.circle(frame, center=(x, y), radius=15, color=(0, 255, 255))
                    index_x=screen_width/frame_width*x
                    index_y=screen_height/frame_height*y
                    # pyautogui.moveTo(index_x,index_y)
                if id == 4:
                    cv2.circle(frame, center=(x, y), radius=15, color=(0, 255, 255))
                    middle_x=screen_width/frame_width*x
                    middle_y=screen_height/frame_height*y
                    pyautogui.moveTo(middle_x, middle_y)
                    # print('outside', abs(index_y-middle_y))
                    if abs(index_y-middle_y)<50:
                        print('click')
                        pyautogui.click()
                        # pyautogui.sleep(1)

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()