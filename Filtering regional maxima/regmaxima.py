# Filtering regional maxima


import numpy as np
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt

from skimage import data
from skimage import img_as_float
from skimage.morphology import reconstruction


image = img_as_float(data.coins())
image = gaussian_filter(image, 1)

seed = np.copy(image)
seed[1:-1, 1:-1] = image.min()
mask = image

dilated = reconstruction(seed, mask, method='dilation')


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 2.5), sharex=True, sharey=True)

ax1.imshow(image)
ax1.set_title('original image')
ax1.axis('off')
ax1.set_adjustable('box-forced')

ax2.imshow(dilated, vmin=image.min(), vmax=image.max())
ax2.set_title('dilated')
ax2.axis('off')
ax2.set_adjustable('box-forced')

ax3.imshow(image - dilated)
ax3.set_title('image - dilated')
ax3.axis('off')
ax3.set_adjustable('box-forced')

fig.tight_layout()

h = 0.4
seed = image - h
dilated = reconstruction(seed, mask, method='dilation')
hdome = image - dilated


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 2.5))

yslice = 197

ax1.plot(mask[yslice], '0.5', label='mask')
ax1.plot(seed[yslice], 'k', label='seed')
ax1.plot(dilated[yslice], 'r', label='dilated')
ax1.set_ylim(-0.2, 2)
ax1.set_title('image slice')
ax1.set_xticks([])
ax1.legend()

ax2.imshow(dilated, vmin=image.min(), vmax=image.max())
ax2.axhline(yslice, color='r', alpha=0.4)
ax2.set_title('dilated')
ax2.axis('off')

ax3.imshow(hdome)
ax3.axhline(yslice, color='r', alpha=0.4)
ax3.set_title('image - dilated')
ax3.axis('off')

fig.tight_layout()
plt.show()