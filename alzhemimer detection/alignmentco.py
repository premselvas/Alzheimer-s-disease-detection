import os
import pydicom
import matplotlib.pyplot as plt

# Path to original dataset
input_folder = r"C:\Users\admin\Desktop\Alzheimer MRI Model\Data set\archive\Alzheimers disease MRI images\AD"
# Path to save PNG images
output_folder = r"C:\Users\admin\Desktop\Alzheimer MRI Model\Data set\converted_dataset\AD"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".dcm"):
        # Read DICOM
        dcm_path = os.path.join(input_folder, filename)
        dicom_data = pydicom.dcmread(dcm_path)
        
        # Save as PNG
        plt.imshow(dicom_data.pixel_array, cmap=plt.cm.gray)
        plt.axis('off')
        plt.savefig(os.path.join(output_folder, filename.replace(".dcm", ".png")), bbox_inches='tight', pad_inches=0)
        plt.close()

print("✅ Conversion completed!")
import pydicom
import numpy as np
from PIL import Image

def load_dicom_image(path):
    dicom_data = pydicom.dcmread(path)
    image_array = dicom_data.pixel_array
    image = Image.fromarray(image_array).convert("RGB")  # Convert to RGB
    return image
