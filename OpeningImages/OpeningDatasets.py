import numpy as np
import struct
import matplotlib.pyplot as plt

# Function to read MNIST images
def load_images(filename):
    with open(filename, 'rb') as f:
        magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
        data = np.frombuffer(f.read(), dtype=np.uint8)
        data = data.reshape(num, rows, cols)
        return data

# Function to read MNIST labels
def load_labels(filename):
    with open(filename, 'rb') as f:
        magic, num = struct.unpack(">II", f.read(8))
        labels = np.frombuffer(f.read(), dtype=np.uint8)
        return labels

# Load your MNIST files
images = load_images(r"C:\Users\Zeus\Desktop\PythonProject\PythonAI\OpeningImages/train-images.idx3-ubyte")
labels = load_labels(r"C:\Users\Zeus\Desktop\PythonProject\PythonAI\OpeningImages/train-labels.idx1-ubyte")


# Show the first 5 images
for i in range(20):
    plt.imshow(images[i], cmap='gray')
    plt.title(f"Label: {labels[i]}")
    plt.show()
