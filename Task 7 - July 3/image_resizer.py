# Import required libraries
from PIL import Image
import os

# Set parameters
input_folder = "input_images"
output_folder = "output_images"
new_size = (800, 800)

# Create output folder if not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through images in folder, resize and convert images
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        try:
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img = img.resize(new_size)

            # Save in PNG format
            new_filename = os.path.splitext(filename)[0] + "_op" + ".png"
            output_path = os.path.join(output_folder, new_filename)
            img.save(output_path)
            print(f"Processed: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
