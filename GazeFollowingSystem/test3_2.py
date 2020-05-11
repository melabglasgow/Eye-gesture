"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

def get():
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
#    text = ""

#    if gaze.is_blinking():
#        text = "Blinking"
#    elif gaze.is_right():
#        text = "Looking right"
#    elif gaze.is_left():
#        text = "Looking left"
#    elif gaze.is_center():
#        text = "Looking center"

#    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = str(gaze.pupil_left_coords())
    right_pupil = str(gaze.pupil_right_coords())
    xx1 = str(int(gaze.eye_left.origin[0]+gaze.eye_left.center[0]))
    yy1 = str(int(gaze.eye_left.origin[1]+gaze.eye_left.center[1]))
    xx2 = str(int(gaze.eye_right.origin[0]+gaze.eye_right.center[0]))
    yy2 = str(int(gaze.eye_right.origin[1]+gaze.eye_right.center[1]))
    re = [left_pupil, xx1, yy1, right_pupil, xx2, yy2]
#    color = (255, 0, 250)    
#    cv2.circle(frame, (xx, yy), 2, color,thickness=3, lineType=8, shift=0)
##    cv2.line(frame, (xx, yy - 5), (xx, yy + 5), color)
#
#
##    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
##    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
#
#    cv2.imshow("Demo", frame)

#    if cv2.waitKey(1) == 27:
#        break

    return re



#while True:
#    print(get())
    
    