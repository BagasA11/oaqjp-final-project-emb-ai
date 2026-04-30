import requests
import json

URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADER={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    payload={ "raw_document": { "text": text_to_analyze } }
    response=requests.post(url,json=payload,headers=HEADER)
    return json.loads(response.text)