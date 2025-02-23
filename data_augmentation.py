# -*- coding: utf-8 -*-
"""Data_Augmentation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LRtFKpjjMN1HEIryOB-C_-yO59Y_b6-M
"""

import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

"""Data augmentation is a technique commonly used in machine learning and deep learning to artificially increase the diversity and size of a dataset by applying various transformations to the original data samples. The goal of data augmentation is to improve the generalization and robustness of machine learning models by exposing them to a wider range of variations and scenarios during training.

In the context of image data, data augmentation typically involves applying geometric transformations, such as rotation, translation, scaling, flipping, and cropping, as well as color transformations, such as brightness adjustment, contrast adjustment, and color shifting. These transformations generate new versions of the original images that retain their semantic content but exhibit variations in appearance.

Data augmentation is particularly useful in scenarios where the available dataset is limited or when the model is prone to overfitting. By augmenting the data, the model is exposed to a larger variety of samples during training, which can help improve its ability to generalize to unseen data and reduce overfitting.

In addition to improving model performance, data augmentation can also help address class imbalance issues in classification tasks by generating additional samples for underrepresented classes.

Overall, data augmentation is a powerful technique for enhancing the quality and quantity of training data, leading to more robust and effective machine learning models.
"""

# Load NIfTI image
image_path = "/content/drive/My Drive/Datasets/nifti/output.nii.gz"
image = nib.load(image_path)
image_data = image.get_fdata()

# Define data augmentation functions
def random_rotation(image_data):
    # Perform random rotation (e.g., 90, 180, or 270 degrees)
    rotation_angle = np.random.choice([90, 180, 270])
    rotated_image_data = np.rot90(image_data, k=rotation_angle//90)
    return rotated_image_data

def random_flip(image_data):
    # Perform random horizontal or vertical flipping
    flip_axis = np.random.choice([0, 1])  # 0: horizontal flip, 1: vertical flip
    flipped_image_data = np.flip(image_data, axis=flip_axis)
    return flipped_image_data

# Example of applying data augmentation
augmented_image_data = random_rotation(image_data)
augmented_image_data = random_flip(augmented_image_data)

# Plot original and augmented images (slices)
original_slice = image_data[:, :, image_data.shape[2] // 2]  # Take a slice from the middle of the image
augmented_slice = augmented_image_data[:, :, augmented_image_data.shape[2] // 2]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_slice, cmap='gray')
plt.title('Original Slice')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(augmented_slice, cmap='gray')
plt.title('Augmented Slice')
plt.axis('off')

plt.show()

"""

*   We import the nibabel library for working with NIfTI images, numpy for numerical operations, and matplotlib.pyplot for visualization.
*   We load a NIfTI image from a specified file path using nib.load() and extract the image data using image.get_fdata().


*   We define two data augmentation functions: random_rotation() for performing random rotation (90, 180, or 270 degrees) and random_flip() for performing random horizontal or vertical flipping.
*   We apply data augmentation by randomly selecting and applying one or more augmentation functions to the original image data.


*   We visualize a slice from both the original and augmented images using matplotlib.






"""