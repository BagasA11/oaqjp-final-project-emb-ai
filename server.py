"""This module are server entrypoint """
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask(__name__)

def __format_output(payload):
    response_txt="For the given statement, the system response is "
    dominant=payload['dominant_emotion']
    del payload['dominant_emotion']
    for k,v in payload.items():
        response_txt+=f"\'{k}\': {v}, "
    response_txt = response_txt.removesuffix(" ")+'.'
    response_txt+=f"The dominant emotion is <b>{dominant}</b>"
    return response_txt

@app.route('/')
def homepage():
    """This controller return index.html"""
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """handle request then return list of emotion in string format"""
    payload=request.args.get('textToAnalyze')
    output=emotion_detector(payload)
    if output is None:
        return ""
    return __format_output(output)
    
if __name__ == "__main__":
    app.run(debug=True)
