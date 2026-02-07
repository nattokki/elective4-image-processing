import cv2
import numpy as np
import os


input_folder = "input_images"
output_folder = "output_images"
os.makedirs(output_folder, exist_ok=True)


def pixelate(img, scale=0.15): 
    h, w = img.shape[:2]
    small = cv2.resize(img, (int(w*scale), int(h*scale)), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)


for file in os.listdir(input_folder):
    if file.lower().endswith((".jpg",".png",".jpeg")):
        path = os.path.join(input_folder, file)
        img = cv2.imread(path)
        if img is None:
            continue
        img = cv2.resize(img, (800, 600))


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


        inverted = cv2.bitwise_not(clean)


        inverted_color = cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)
        pixelated = pixelate(inverted_color, scale=0.20)


        name = os.path.splitext(file)[0]
        cv2.imwrite(f"{output_folder}/{name}_output.jpg", pixelated)

print("Done processing all images!")

