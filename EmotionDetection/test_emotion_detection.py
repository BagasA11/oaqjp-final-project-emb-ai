import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_joy(self):
        case_='I am glad this happened'
        expected_value='joy'
        response=emotion_detector(case_)
        test_=response['dominant_emotion']
        self.assertEqual(test_,expected_value)
    
    def test_emotion_anger(self):
        case_='I am really mad about this'
        expected_value='anger'
        response=emotion_detector(case_)
        test_=response['dominant_emotion']
        self.assertEqual(test_,expected_value)
    
    def test_emotion_disgust(self):
        case_='I feel disgusted just hearing about this'
        expected_value='disgust'
        response=emotion_detector(case_)
        test_=response['dominant_emotion']
        self.assertEqual(test_,expected_value)
    
    def test_emotion_sadness(self):
        case_='I am so sad about this'
        expected_value='sadness'
        response=emotion_detector(case_)
        test_=response['dominant_emotion']
        self.assertEqual(test_,expected_value)
    
    def test_emotion_fear(self):
        case_='I am really afraid that this will happen'
        expected_value='fear'
        response=emotion_detector(case_)
        test_=response['dominant_emotion']
        self.assertEqual(test_,expected_value)

if __name__ == '__main__':
    unittest.main()