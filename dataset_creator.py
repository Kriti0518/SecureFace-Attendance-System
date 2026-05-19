import cv2
import os

DATASET_DIR = "face_dataset"

if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def add_employee():

    name = input("Enter employee name: ")

    user_folder = os.path.join(DATASET_DIR, name)

    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    count = 0

    print("Capturing face images... Press Q to quit")

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Camera not working")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:

            face = frame[y:y+h, x:x+w]

            count += 1

            file_path = os.path.join(user_folder, f"{count}.jpg")

            cv2.imwrite(file_path, face)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.imshow("Face Capture", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if count >= 20:
            break

    cap.release()
    cv2.destroyAllWindows()

    print(f"{count} face images saved for {name}")