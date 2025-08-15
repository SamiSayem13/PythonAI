from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Load dataset
(_, _), (test_images, test_labels) = mnist.load_data()

# Show first test image
plt.imshow(test_images[0], cmap='gray')
plt.title(f"Label: {test_labels[0]}")
plt.show()
