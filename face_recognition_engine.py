import cv2
from attendance_manager import mark_attendance

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def start_attendance_system():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    print("Starting SecureFace Attendance System...")
    print("Press Q to quit")

    attendance_marked = False

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Camera not working")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

            if not attendance_marked:

                mark_attendance("Detected_User")

                attendance_marked = True

        cv2.imshow("SecureFace Attendance System", frame)

        key = cv2.waitKey(10) & 0xFF

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()