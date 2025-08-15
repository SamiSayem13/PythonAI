import numpy as np
import struct
import matplotlib.pyplot as plt

# Load MNIST images
def load_images(filename):
    with open(filename, 'rb') as f:
        magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
        data = np.frombuffer(f.read(), dtype=np.uint8)
        data = data.reshape(num, rows, cols)
        return data

# Load MNIST labels
def load_labels(filename):
    with open(filename, 'rb') as f:
        magic, num = struct.unpack(">II", f.read(8))
        labels = np.frombuffer(f.read(), dtype=np.uint8)
        return labels

# Update these paths to where your files are
images = load_images("C:/Users/Zeus/Desktop/PythonProject/OpeningImages/t10k-images-idx3-ubyte")
labels = load_labels("C:/Users/Zeus/Desktop/PythonProject/OpeningImages/t10k-labels-idx1-ubyte")

# Scroll through images interactively
index = 0
while True:
    plt.imshow(images[index], cmap='gray')
    plt.title(f"Label: {labels[index]}")
    plt.show()
    
    cmd = input("Press Enter for next image, or type q to quit: ")
    if cmd.lower() == 'q':
        break
    index += 1
    if index >= len(images):
        print("End of dataset")
        break
