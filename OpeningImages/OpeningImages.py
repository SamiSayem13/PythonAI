import tensorflow as tf
import matplotlib.pyplot as plt

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# Show first test image
plt.imshow(test_images[0], cmap='gray')
plt.title(f"Label: {test_labels[0]}")
plt.show()
