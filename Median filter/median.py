import numpy as np
import scipy.misc
from scipy import ndimage
import matplotlib.pyplot as plt

f = scipy.misc.face(gray=True)
f = f[230:290, 220:320]
noisy = f + 0.4*f.std()*np.random.random(f.shape)
med_denoised = ndimage.median_filter(noisy, 3)
plt.figure(figsize=(12,2.8))
plt.subplot(121)
plt.imshow(noisy, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.axis('off')
plt.title('noisy', fontsize=16)
plt.subplot(122)
plt.imshow(med_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.axis('off')
plt.title('Median filter', fontsize=16)
plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0, right=1)
plt.show()