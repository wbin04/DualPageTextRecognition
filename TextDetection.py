from PIL import Image
import numpy as np
from paddleocr import PaddleOCR
import cv2
class TextDetection():
    def __init__(self):
        self.detector = PaddleOCR(use_angle_cls=True, lang='en', use_pdserving=False, det_db_thresh=0.3, det_db_box_thresh=0.5)

    def __call__(self, img_path):
        results = self.detector.ocr(img_path, cls=False)
    
        bounding_boxes = []
        
        for line in results:
            for word_info in line:
                points = word_info[0]
                bounding_boxes.append(points)
        
        detected_lines = []
        img = Image.open(img_path)
        img_cv2 = cv2.imread(img_path)
        padding = 10

        for bbox in bounding_boxes:
            x_topLeft, y_topLeft = map(int, bbox[0])
            x_botRight, y_botRight = map(int, bbox[2])

            y_topLeft = max(0, y_topLeft - padding)
            y_botRight = min(img.height, y_botRight + padding)

            region = img_cv2[y_topLeft:y_botRight, x_topLeft:x_botRight]

            if region is not None and region.size > 0:
                gray_region = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
                _, thresh = cv2.threshold(gray_region, 240, 255, cv2.THRESH_BINARY)
                white_ratio = np.sum(thresh == 255) / (thresh.size)

                if white_ratio < 0.9:
                    cropped_img = self.crop_image(img, (x_topLeft, y_topLeft, x_botRight, y_botRight))
                    if cropped_img is not None:
                        detected_lines.append(cropped_img)

        return detected_lines
        
    @staticmethod
    def crop_image(img, bbox):
        cropped_img = img.crop(bbox).convert("RGB")

        return cropped_img
