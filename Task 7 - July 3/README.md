# Image Resizer Tool - Python Pillow App
A batch image processing tool built using **Python** and **Pillow**, designed to automate resizing of multiple images by fixed dimensions or convert formats. This script handles `.jpg`, `.jpeg`, and `.png` files, resizes them to a desired resolution (default 800×800), and saves them into a separate output directory with optimized file size.


## Features
- **Batch Image Resizing**: Resizes all supported images in a folder at once
- **File Format Conversion**: Automatically converts PNG to JPG
- **Optimized Output Size**: Saves images with reduced file size using `optimize` and `quality`
- **Error Handling**: Skips unsupported or broken images with meaningful logs
- **Folder Isolation**: Input and output images are kept in separate folders
- **Extensible Logic**: Can be extended for compression by file size, GUI, CLI arguments, etc.

## Implementation Overview
## Implementation Overview
- **Library Used**: Python Imaging Library (Pillow)
- **Image Formats Supported**: `.jpg`, `.jpeg`, `.png`
- **Resize Mechanism**: `img.resize((width, height))`
- **File Compression**: Saves with `optimize=True` and reduced `quality` for JPEGs
- **Conversion**: PNGs are converted to RGB mode before saving as JPEG


## Folder Structure
Task 7 - July 3/
│
├── input_images/  
│   ├── IMG_1.jpg  
│   ├── IMG_2.jpeg  
│   ├── IMG_3.png  
│
├── output_images/  
│   └── IMG_1.jpg  
│   └── IMG_2.jpg  
│   └── IMG_3.jpg  
│
├── main.py  
├── README.md  

## Screenshots

## Getting started
1. Clone this repository to your local machine.

   ```
    https://github.com/RohitBhavsar27/Elevate-Labs-Internship.git
   ```
   ```
    cd 'Task 7 - July 3'
   ```

2. Install the required dependency:

    ```
    pip install pillow
    ```

3. Add some images in the `input_images/` folder. Supported formats: `.jpg`, `.jpeg`, `.png`.

4. Run the script:

    ```bash
    python image_resizer.py
    ```

5. Resized and converted images will appear in the `output_images/` folder.

## Acknowledgments
This tool was developed as part of the Elevate Labs Internship under the Ministry of MSME, Govt. of India. It reinforces practical knowledge of file handling, image processing, and exception handling using Python.

## License
This project is released under the MIT License. Feel free to use and learn!

