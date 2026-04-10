# 7a_error_handling_function.py

import requests
import json

def emotion_detector(text_to_analyze):
    """
    Calls emotion detection API and handles errors including HTTP 400.
    Returns emotions or error message.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=5)

        # Handle HTTP 400 explicitly
        if response.status_code == 400:
            return {
                "error": "Bad Request (400): Invalid input provided. Please check the text."
            }

        # Handle other non-success responses
        if response.status_code != 200:
            return {
                "error": f"Request failed with status code {response.status_code}",
                "details": response.text
            }

        # Parse successful response
        return response.json()

    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Please try again."}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# Example usage
if __name__ == "__main__":
    text = "I am very happy today!"
    result = emotion_detector(text)
    print(json.dumps(result, indent=2))