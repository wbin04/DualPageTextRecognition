from vietocr.tool.config import Cfg
from vietocr.tool.predictor import Predictor

class TextRecognition():
    def __init__(self, device = 'cpu'):
        config = Cfg.load_config_from_name('vgg_transformer')
        config['device'] = device
        self.recognizer = Predictor(config)

    def __call__(self, img):
        text, confidence = self.recognizer.predict(img, return_prob = True)
        return text, confidence
    
