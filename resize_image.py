from PIL import Image
import os

def preprocess_images(input_dir, output_dir, size=128):
    os.makedirs(output_dir, exist_ok=True)
    for file in os.listdir(input_dir):
        if file.endswith(('.jpg', '.png')):
            img = Image.open(os.path.join(input_dir, file)).convert('RGB')
            img = img.resize((size, size))
            img.save(os.path.join(output_dir, file))

preprocess_images('data/Faces', 'data/Processed_Image', size=128)
