# ELECTIVE4 IMAGE PROCESSING PROJECT
## Project Overview
This project applies **image processing techniques** using Python and OpenCV.  
It automatically processes images from the `input_images/` folder and saves the results to the `output_images/` folder.  

The processing pipeline applies **five sequential techniques** to each image:

1. Grayscale Conversion  
2. Gaussian Blur  
3. Adaptive Threshold  
4. Morphological Closing  
5. Inversion & Pixelation  

Continuous Integration (CI) using **GitHub Actions** ensures the code is tested and validated automatically on every push.

---
## Tools and Technologies
- Python 3
- OpenCV (opencv-python)
- NumPy
- GitHub
- GitHub Actions (CI)
- PyTest

---
## System Features
1. Automatically detects image files in `input_images/`  
2. Applies the following image processing techniques sequentially:
   - **Grayscale Conversion** – converts colored images to black and white  
   - **Gaussian Blur** – smooths the image to reduce noise  
   - **Adaptive Threshold** – converts image to binary based on local pixel intensity  
   - **Morphological Closing** – removes small holes and cleans object edges  
   - **Inversion & Pixelation** – inverts colors and pixelates the image for final output  
3. Saves processed images to `output_images/`  
4. CI pipeline runs automatically on every GitHub push  

---
## Project Structure
```text
ELECTIVE4-IMAGE-PROCESSING/
│── .github/workflows/ 
│── input_images/ 
│── output_images/ 
│── .gitignore 
│── invert_pixel.py 
│── README.md 
│── requirements.txt 
```
---
## How to Run the Project

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the program:

```bash
python invert_pixel.py
```

3. Processed images will appear in the ***output_images/*** folder.
   
---
## Running Tests

To run automated tests:

```bash
pytest
```

---
## Continuous Integration (CI) Section
This project uses **GitHub Actions** to automatically:
- Install dependencies  
- Run automated tests (if any)  
- Validate system build  

The pipeline runs on every **push to GitHub**.  

---
## Group Roles
- Image Processing Lead – Implements image processing pipeline
- DevOps Engineer – Configures GitHub Actions
- Tester – Writes automated tests
- Documenter/Presenter – Prepares README and presentation
  
---
## DevOps Workflow

```text
Developer → GitHub Push → GitHub Actions → Run Tests → Build Success → Output Images
```
- Every commit triggers the CI pipeline
- Ensures code reliability and automation
- Tracks development progress through Git commit history
  
---
## Example Output

```
Original Image → Final Processed Image
```
*The final image demonstrates all five processing techniques applied sequentially.*

---
