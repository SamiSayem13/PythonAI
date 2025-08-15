import struct
import numpy as np
import random
import matplotlib.pyplot as plt

# -------------------------
# Functions to load MNIST
# -------------------------
def load_images(filename):
    with open(filename, 'rb') as f:
        magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
        data = np.frombuffer(f.read(), dtype=np.uint8)
        data = data.reshape(num, rows, cols)
        return data

def load_labels(filename):
    with open(filename, 'rb') as f:
        magic, num = struct.unpack(">II", f.read(8))
        labels = np.frombuffer(f.read(), dtype=np.uint8)
        return labels

# -------------------------
# Paths to your files
# -------------------------
training_images_filepath = r'C:\Users\Zeus\Desktop\PythonProject\PythonAI\OpeningImages\train-images.idx3-ubyte'
training_labels_filepath = r'C:\Users\Zeus\Desktop\PythonProject\PythonAI\OpeningImages\train-labels.idx1-ubyte'
test_images_filepath = r'C:\Users\Zeus\Desktop\PythonProject\PythonAI\OpeningImages\t10k-images.idx3-ubyte'
test_labels_filepath = r'C:\Users\Zeus\Desktop\PythonProject\PythonAI\OpeningImages\t10k-labels.idx1-ubyte'

# -------------------------
# Load the datasets
# -------------------------
x_train = load_images(training_images_filepath)
y_train = load_labels(training_labels_filepath)
x_test = load_images(test_images_filepath)
y_test = load_labels(test_labels_filepath)

# -------------------------
# Helper function to show images
# -------------------------
def show_images(images, title_texts):
    cols = 5
    rows = int(len(images)/cols) + 1
    plt.figure(figsize=(30,20))
    for index, (img, title) in enumerate(zip(images, title_texts), start=1):
        plt.subplot(rows, cols, index)        
        plt.imshow(img, cmap=plt.cm.gray)
        if title != '':
            plt.title(title, fontsize=15)

# -------------------------
# Show some random images
# -------------------------
images_2_show = []
titles_2_show = []

# 10 random training images
for i in range(10):
    r = random.randint(0, 59999)
    images_2_show.append(x_train[r])
    titles_2_show.append(f'training image [{r}] = {y_train[r]}')

# 5 random test images
for i in range(5):
    r = random.randint(0, 9999)
    images_2_show.append(x_test[r])
    titles_2_show.append(f'test image [{r}] = {y_test[r]}')

show_images(images_2_show, titles_2_show)
plt.show()
