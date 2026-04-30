import requests
import json

URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADER={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def __dominant_emotion_format(response:dict):
   response=response['emotionPredictions']['emotion']
   del response['target']
   del response['emotionMentions']
   max_key='';max_value=0.0
   for k,v in response.items():
      if v > max_value:
         max_key=k 
         max_value=v
   response['dominant_emotion']=max_key
   return response
        
def emotion_detector(text_to_analyze):
   payload={ "raw_document": { "text": text_to_analyze } }
   response=requests.post(URL,json=payload,headers=HEADER)
   response=json.loads(response.text)
   return __dominant_emotion_format(response)

EXAMPLE='Pentingnya PENDIDIKAN! Daripada jadi DUNGU macam supir² yg menghadang'
