import os
import cv2
import mediapipe as mp

#--Main Mediapipe Face Recognition logic--#
def detectFace(img):
    H, W, _ = img.shape
    mp_face_detection = mp.solutions.face_detection
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        out = face_detection.process(img_rgb)

        if out.detections is not None:
            for detection in out.detections:
                bbox = detection.location_data.relative_bounding_box

                x1 = int(bbox.xmin * W)
                y1 = int(bbox.ymin * H)
                w = int(bbox.width * W)
                h = int(bbox.height * H)

                # Fix coordinates to stay within bounds
                x1 = max(0, x1)
                y1 = max(0, y1)
                x2 = min(W, x1 + w)
                y2 = min(H, y1 + h)

                if x2 > x1 and y2 > y1:  # Ensure region is valid
                    face_region = img[y1:y2, x1:x2] 
                    img[y1:y2, x1:x2] = cv2.blur(face_region, (50, 50))
    return img


#---Function for Image Face anonymize ---#
def ImageAnonymize(img_path):
    actual_image = cv2.imread(img_path)
    img = cv2.resize(actual_image,(440,680))
    detectFace(img)
    cv2.imshow('img',img)
    cv2.waitKey(0)

#---Function for Video Face anonymize---#
def VideoAnonimize(video_path):
    video = cv2.VideoCapture(video_path)
    ret = True
    while ret:
        ret,frame = video.read()
        if ret:
            detectFace(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(40) & 0xFF == ord('q'):
                break
    video.release()
    cv2.destroyAllWindows()
    
#---Function for Live webcam Face anonymize--#
def LiveAnonymize():
    webcam = cv2.VideoCapture(0)

    while True:
        ret,frame = webcam.read()
        detectFace(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    
#--Main Function--#
if __name__ == "__main__":
    value = input("\n1.For Live Face Anonymize\n2.For Face Anoymization of image\n3.For Face Anonyzation on video: ")
    if value == "1":
        LiveAnonymize()     
    elif value == "2":
        img_path = os.path.join('.','data','me.jpg')
        ImageAnonymize(img_path)
    elif value == "3":
        video_path = os.path.join('.','data','test2.mp4')
        VideoAnonimize(video_path)
    else:
        print("Wrong Choice!")
    