from flask import Flask, requests, make_response
from EmotionDetection.emotion_detection import emotion_detector

app=Flask()

@app.get('/')
def detect_emotion():
    input=requests.args.get('input')
    output=emotion_detector(input)
    response_txt="For the given statement, the system response is "
    dominant=output['dominant_emotion']
    del output['dominant_emotion']
    for k,v in output.items():
        response_txt+=f"\'{k}\':{v}, "
    response_txt = response_txt.removesuffix(" ")+'.'
    response_txt+=f"The dominant emotion is <b>{dominant}</b>"
    # 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy."
    return response_txt