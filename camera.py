import tensorflow as tf
import cv2
import numpy as np
from keras.preprocessing import image

model = tf.keras.models.load_model('mymodel.h5')

final_results = {0: 'mask', 1: 'without mask'}
GR_dict = {0: (0, 255, 0), 1: (0, 0, 255)}

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        faces = face_cascade.detectMultiScale(frame, 1.05, 5)
        for x, y, w, h in faces:

            face_img = frame[y:y + h, x:x + w]
            # resized = np.array(face_img,target_size=(128,128))
            resized = cv2.resize(face_img, (150, 150))
            # normalized = resized/255.0
            reshaped = resized.reshape(1, 150, 150, 3)
            result = np.round(model.predict(reshaped))
            print(result)

            # label = np.argmax(result,axis=1)[0]

            if result == 0:
                cv2.rectangle(frame, (x, y), (x + w, y + h), GR_dict[1], 2)
                cv2.rectangle(frame, (x, y - 40), (x + w, y), GR_dict[1], -1)
                cv2.putText(frame, final_results[1], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), GR_dict[0], 2)
                cv2.rectangle(frame, (x, y - 40), (x + w, y), GR_dict[0], -1)
                cv2.putText(frame, final_results[0], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()