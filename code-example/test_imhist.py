import cv2
import numpy as np
from imhist import imhist, imcdf
import matplotlib.pyplot as plt

img = cv2.imread('assets/Plane.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
v = hsv[:, :, 2].copy()

v_hist = imhist(v, PMF=False)
v_pmf = imhist(v, PMF=True)
v_cdf = imcdf(v)

plt.figure(num=1)
plt.plot(np.arange(256), v_hist, 'b', label='Histogram')
plt.ylabel('Number of Occurrences')
plt.xlabel('Brightness')
plt.grid(which="both")
plt.legend()

plt.figure(num=2)
plt.plot(np.arange(256), v_pmf, 'g', label='PMF')
plt.ylabel('Probability Mass Function')
plt.xlabel('Brightness')
plt.grid(which="both")
plt.legend()

plt.figure(num=3)
plt.plot(np.arange(256), v_cdf, 'r', label='CDF')
plt.ylabel('Cumulative Distribution Function')
plt.xlabel('Brightness')
plt.grid(which="both")
plt.legend()
plt.show()


