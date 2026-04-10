# 7b_error_handling_server.py

from flask import Flask, request, jsonify
from 7a_error_handling_function import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def emotion_analysis():
    """
    Emotion detection endpoint with blank input (bad input) handling.
    """

    text_to_analyze = request.args.get("text")

    # -------------------------------
    # Handle missing or blank input
    # -------------------------------
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return jsonify({
            "error": "400 Bad Request: Input text is empty or missing."
        }), 400

    # Call emotion detection function
    result = emotion_detector(text_to_analyze)

    # If function returned error
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 400

    # Extract emotions safely (based on Watson response structure)
    try:
        emotions = result["emotionPredictions"][0]["emotion"]

        response = {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0)
        }

        # Find dominant emotion
        dominant_emotion = max(response, key=response.get)
        response["dominant_emotion"] = dominant_emotion

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "error": "Failed to parse emotion response",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)