import cv2
import numpy as np
import os

# Folders
input_folder = "input_images"
output_folder = "output_images"
os.makedirs(output_folder, exist_ok=True)

# Pixelate function
def pixelate(img, scale=0.15):  # smaller scale = more pixelated
    h, w = img.shape[:2]
    small = cv2.resize(img, (int(w*scale), int(h*scale)), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)

# Process all images in input folder
for file in os.listdir(input_folder):
    if file.lower().endswith((".jpg",".png",".jpeg")):
        path = os.path.join(input_folder, file)
        img = cv2.imread(path)
        img = cv2.resize(img, (800, 600))

        # --- Combo 3 ---
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        th = cv2.adaptiveThreshold(
            blur, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11, 2
        )
        kernel = np.ones((3,3), np.uint8)
        clean = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

        # --- Invert ---
        inverted = cv2.bitwise_not(clean)

        # --- Pixelate ---
        inverted_color = cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)
        pixelated = pixelate(inverted_color, scale=0.20)

        # --- Save ---
        name = os.path.splitext(file)[0]
        cv2.imwrite(f"{output_folder}/{name}_output.jpg", pixelated)

print("Done processing all images!")
