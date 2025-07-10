from PIL import Image
import numpy as np

# Open and convert the image to grayscale
img = Image.open("/home/sawmin/python_learning/learn/image.jpg").convert("L")  # 'L' mode = grayscale
img = img.resize((28, 28))  # Resize if not already 28x28

pixels = np.array(img)
for pixel in pixels:
    for i in pixel:
        print(i, end=' ')
    print()  # Newline after printing all pixel values
print("Image size:", pixels.shape)
pixels = pixels / 255.0  # Normalize values to range [0, 1]
input_vector = pixels.flatten()  # Flatten the 2D array to 1D
print(len(input_vector), "pixels in the input vector")
#print("Input vector:", input_vector)   