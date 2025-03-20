import subprocess
import os
import shutil
from PIL import Image
import cv2

class Dewarper:
    def __init__(self, output_dir="dewarped_output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True) 

    def dewarp(self, image_path):
        print(f"Processing dewarp for: {image_path}")
        try:
            result = subprocess.run(['page-dewarp', image_path], capture_output=True, text=True, check=True)

        except subprocess.CalledProcessError as e:
            return None

        base_name = os.path.splitext(os.path.basename(image_path))[0]
        possible_outputs = [f"{base_name}_dewarped.png", f"{base_name}_thresh.png"]
        
        for output_file in possible_outputs:
            if os.path.exists(output_file):
                output_path = os.path.join(self.output_dir, output_file)
                shutil.move(output_file, output_path) 
                print(f"Saved dewarped image: {output_path}")

                return output_path
        return None
    
    def split_image_with_offset(self, image_path, offset_ratio=0.06):
        image = cv2.imread(image_path)
        
        height, width, _ = image.shape

        offset = int(width * offset_ratio)
        middle = width // 2

        left_part = image[:, :middle + offset]
        right_part = image[:, middle - offset:]

        left_path = "book_left_adjusted.jpg"
        right_path = "book_right_adjusted.jpg"
        cv2.imwrite(left_path, left_part)
        cv2.imwrite(right_path, right_part)

        return left_path, right_path

    def process_image(self, image_path):
        dewarper = Dewarper(self.output_dir)
        
        left_image, right_image = self.split_image_with_offset(image_path)
        
        left_dewarped = dewarper.dewarp(left_image)
        right_dewarped = dewarper.dewarp(right_image)
        
        dewarped_images = []
        if left_dewarped:
            dewarped_images.append(left_dewarped)
        if right_dewarped:
            dewarped_images.append(right_dewarped)
            
        if os.path.exists(left_image):
            os.remove(left_image)
        if os.path.exists(right_image):
            os.remove(right_image)
            
        return dewarped_images
