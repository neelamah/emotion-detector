from flask import Flask, request, jsonify
from emotion_detector import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect():
    text = request.args.get('text')

    if not text:
        return jsonify({"error": "Invalid input"}), 400

    result = emotion_detector(text)

    return jsonify(result)


if __name__ == "__main__":
    print("Import successful")

    test_text = "I love this course"
    print("Testing emotion detector...")

    result = emotion_detector(test_text)

    print("Input:", test_text)
    print("Output:", result)

    print("Test completed successfully")