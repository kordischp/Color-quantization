# -*- coding: utf-8 -*-
"""
==================================
Color Quantization using K-Means
==================================

Performs a pixel-wise Vector Quantization (VQ) of an image, reducing the number of colors required to show the image,
then saves the images created using K-means and random methods. K-means finds average colors to use for modified image,
random method selects them at random from the original image. Random method sometimes can give better results at low color number.

The program has an option to resize an image before performing color quantization - useful for creating nonograms.

"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from time import time
from PIL import Image
import skimage
from pathlib import Path


# Parameters
fname = 'image.jpg'   # File name, if not found - a sample image is used.
n_colors = 10      # Reduce number of colors to this value.
pixelize = False   # Reduce size of image before performing color quantization? True/False.
fsize = (60,80)    # Target size of pixelated image.



# Load image, if file not found - sample below will be loaded.
try:
    pic = Image.open(fname)
    print(f"Loaded image '{fname}'.")
except FileNotFoundError:
    pic = load_sample_image("china.jpg")
    print(f"File '{fname}' not found. Loaded sample image instead.")
    fname = 'sample.jpg'
    pic = skimage.img_as_ubyte(pic)
    skimage.io.imsave(fname, pic)
    pic = Image.open(fname)


# Pixelize image if desired. 
if pixelize:
    pic = pic.resize(fsize)
    print("Images have been pixelized.")
else:
    print("Pixelization skipped.")


# Convert to floats instead of the default 8 bits integer coding. Dividing by
# 255 is important so that plt.imshow works well on float data (needs to be in the range [0-1])
pic = np.array(pic, dtype=np.float64) / 255

# Load Image and transform to a 2D numpy array.
w, h, d = original_shape = tuple(pic.shape)
assert d == 3
image_array = np.reshape(pic, (w * h, d))

print("Fitting model on a small sub-sample of the data")
t0 = time()
image_array_sample = shuffle(image_array, random_state=0, n_samples=1_000)
kmeans = KMeans(n_clusters=n_colors, n_init="auto", random_state=0).fit(
    image_array_sample
)
print(f"done in {time() - t0:0.3f}s.")

# Get labels for all points
print("Predicting color indices on the full image (k-means)")
t0 = time()
labels = kmeans.predict(image_array)
print(f"done in {time() - t0:0.3f}s.")


codebook_random = shuffle(image_array, random_state=0, n_samples=n_colors)
print("Predicting color indices on the full image (random)")
t0 = time()
labels_random = pairwise_distances_argmin(codebook_random, image_array, axis=0)
print(f"done in {time() - t0:0.3f}s.")

# Display all results, alongside original image
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Original image
axs[0].imshow(pic)
axs[0].axis("off")
axs[0].set_title("Original image")

# K-Means method quantized image
axs[1].imshow(kmeans.cluster_centers_[labels].reshape(w, h, -1))
axs[1].axis("off")
axs[1].set_title(f"Quantized image ({n_colors} colors, K-Means)")

# Random method quantized image
axs[2].imshow(codebook_random[labels_random].reshape(w, h, -1))
axs[2].axis("off")
axs[2].set_title(f"Quantized image ({n_colors} colors, Random)")

plt.tight_layout()
plt.show()


# Save quantized image to files
pic = kmeans.cluster_centers_[labels].reshape(w, h, -1)
pic = skimage.img_as_ubyte(pic)
skimage.io.imsave(Path(fname).stem + '_kmeans.png', pic)

pic = codebook_random[labels_random].reshape(w, h, -1)
pic = skimage.img_as_ubyte(pic)
skimage.io.imsave(Path(fname).stem + '_random.png', pic)




"""
This code is a modification of the following code:

Authors: Robert Layton <robertlayton@gmail.com>
         Olivier Grisel <olivier.grisel@ensta.org>
         Mathieu Blondel <mathieu@mblondel.org>
License: BSD 3 clause
Source:  https://scikit-learn.org/stable/auto_examples/cluster/plot_color_quantization.html
"""