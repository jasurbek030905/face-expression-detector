import cv2
from fer import FER

# Initialize emotion detector
detector = FER(mtcnn=False)

# Start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotions
    results = detector.detect_emotions(frame)

    for result in results:
        x, y, w, h = result["box"]
        emotions = result["emotions"]

        # Get highest emotion
        emotion = max(emotions, key=emotions.get)
        score = emotions[emotion]

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Show label
        label = f"{emotion}: {score:.2f}"
        cv2.putText(frame, label, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("Emotion Detector", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()