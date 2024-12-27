import os
import shutil

# Define source and target directories
source_dir = '/Users/amanattar/Documents/1 My Computer/Project/StyleGAN/lfw'  # The root directory of your LFW dataset
target_dir = '/Users/amanattar/Documents/1 My Computer/Project/StyleGAN/Data/Faces'  # The directory to store all images

# Create the target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Walk through all subdirectories
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # Check if the file is an image
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            source_path = os.path.join(root, file)
            target_path = os.path.join(target_dir, file)
            
            # Ensure unique file names (avoid overwriting)
            base, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(target_path):
                target_path = os.path.join(target_dir, f"{base}_{counter}{ext}")
                counter += 1

            # Move the file
            shutil.copy(source_path, target_path)

print(f"All images have been copied to {target_dir}")
