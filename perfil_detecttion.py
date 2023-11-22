import cv2
import time
import imutils
import BoundingBox
import f_detector

# instanciar detector
detector = f_detector.detect_face_orientation()

# visualizar
cv2.namedWindow("preview")
cam = cv2.VideoCapture(0)
while True:
    # read the frame from the camera and send it to the server
    star_time = time.time()
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame = imutils.resize(frame,width=720)
    #-------------------------- Insertar preproceso -------------------------------------
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detectar si hay un rostro frontal o de perfil
    w = "A"
    boxes,names,w1,w2,w3 = detector.face_orientation(gray)
    print(names)


    if ['frontal'] == names:
        w=str(w1)
    # elif names[0] == 'left':
    #     w=str(w2)
    # elif names[0] == 'right':
    #     w=str(w3)
    
        frame = BoundingBox.bounding_box(frame,boxes,w,names)

    # print(w1)
    # print(w2)
    # print(w3)

    # ----------------------------------------------------------------------------
    end_time = time.time() - star_time    
    FPS = 1/end_time


    cv2.putText(frame,f"FPS: {round(FPS,3)}",(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

    cv2.imshow('preview',frame)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break