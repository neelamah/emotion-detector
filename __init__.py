from .emotion_detector import emotion_detector


result = emotion_detector("I am happy")

with open("4b_packaging_test.txt", "w") as file:
    file.write("EmotionDetection is a valid package")