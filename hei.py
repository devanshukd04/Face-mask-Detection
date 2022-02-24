import tensorflow as tf
import numpy as np
import cv2
from keras.preprocessing import image
import matplotlib.pyplot as plt
model = tf.keras.models.load_model('mymodel.h5')
final_results={0:'mask',1:'without mask'}
GR_dict={0:(0,255,0),1:(0,0,255)}
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    #     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.05, 5)

    for x, y, w, h in faces:

        face_img = img[y:y + h, x:x + w]
        #         resized = np.array(face_img,target_size=(128,128))
        resized = cv2.resize(face_img, (150, 150))
        #         normalized = resized/255.0
        reshaped = resized.reshape(1, 150, 150, 3)
        result = np.round(model.predict(reshaped))
        print(result)

        #         label = np.argmax(result,axis=1)[0]

        if result == 0:
            cv2.rectangle(img, (x, y), (x + w, y + h), GR_dict[1], 2)
            cv2.rectangle(img, (x, y - 40), (x + w, y), GR_dict[1], -1)
            cv2.putText(img, final_results[1], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), GR_dict[0], 2)
            cv2.rectangle(img, (x, y - 40), (x + w, y), GR_dict[0], -1)
            cv2.putText(img, final_results[0], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow('LIVE', img)
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()