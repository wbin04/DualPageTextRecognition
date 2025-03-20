from PIL import Image
from TextRecognition import TextRecognition
from TextDetection import TextDetection
import matplotlib.pyplot as plt
from dewarper import Dewarper

class FullPipelineOCR():
    def __init__(self):
        self.dewarper = Dewarper()
        self.detector = TextDetection()
        self.recognizer = TextRecognition()
    
    def __call__(self, img_path):
        dewarped_images = self.dewarper.process_image(img_path)
        all_paragraphs = []
        for dewarped_img_path in dewarped_images:
            detected_images = self.detector(dewarped_img_path)
            text_lines = []
            for img in detected_images:
                text, confidence = self.recognizer(img)
                text_lines.append(text)
            paragraphs = self.merge_sentences(text_lines)
            all_paragraphs.extend(paragraphs)
        return all_paragraphs

    def merge_sentences(self, text_lines):
        paragraphs = []
        current_sentence = ""
        
        for line in text_lines:
            if "..." in line:
                parts = line.split("...")
                
                current_sentence += parts[0] + "..."
                paragraphs.append(current_sentence.strip())
                current_sentence = ""
                
                if len(parts) > 1 and parts[1]:
                    current_sentence = parts[1]
                continue

            if "." in line and not line.endswith("..."):
                parts = line.split(".")
                
                current_sentence += " " + parts[0] + "."
                paragraphs.append(current_sentence.strip())
                current_sentence = ""
                
                if len(parts) > 1:
                    current_sentence = ".".join(parts[1:])
            else:
                current_sentence += " " + line
        if current_sentence.strip():
            paragraphs.append(current_sentence.strip())
        
        return paragraphs
        