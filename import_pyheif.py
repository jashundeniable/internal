import pyheif
from PIL import Image
import os

def convert_heic_to_png ( heic_path, output_path):
    heif_file = pyheif.read(heic_path)

    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    image.save(output_path, format="PNG")

# Get the absolute paths for the HEIC file and desired PNG output
  
script_dir = os.path.dirname(os.path.abspath(__file__))
heic_path = os.path.join(script_dir, '..', '..', 'Desktop', 'to-read-learn', 'IMG_8712.heic')
output_path = os.path.join(script_dir, '..', '..', 'Desktop', 'to-read-learn', 'IMG_8712.PNG')

# Print the constructed paths
print("HEIC file path:", heic_path)
print("Output file path:", output_path)

# Call the conversion function
convert_heic_to_png(heic_path, output_path)

