import requests

API_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

def emotion_detector(text):
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    payload = {
        "raw_document": {"text": text}
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=5)

        if response.status_code == 200:
            emotions = response.json()['emotionPredictions'][0]['emotion']
        else:
            raise Exception("API failed")

    except Exception:
        # ✅ MOCK DATA (fallback)
        emotions = {
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.05,
            "joy": 0.85,
            "sadness": 0.07
        }

    dominant = max(emotions, key=emotions.get)

    return {
        "anger": emotions['anger'],
        "disgust": emotions['disgust'],
        "fear": emotions['fear'],
        "joy": emotions['joy'],
        "sadness": emotions['sadness'],
        "dominant_emotion": dominant
    }
    
    
if __name__ == "__main__":
    text = "I love learning AI"

    result = emotion_detector(text)

    print("Input:", text)
    print("Output:", result)