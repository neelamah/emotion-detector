from flask import Flask, request, render_template_string
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Simple HTML page (no separate template needed)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Emotion Detector</title>
</head>
<body>
    <h2>Emotion Detection Web App</h2>

    <form method="POST">
        <input type="text" name="text" placeholder="Enter text here" size="50">
        <button type="submit">Analyze</button>
    </form>

    {% if result %}
        <h3>Result:</h3>
        <p><b>Input:</b> {{ text }}</p>
        <p><b>Dominant Emotion:</b> {{ result['dominant_emotion'] }}</p>
        <p><b>Full Output:</b> {{ result }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        result = emotion_detector(text)

    return render_template_string(HTML_PAGE, result=result, text=text)


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)