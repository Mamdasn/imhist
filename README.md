[![PyPI Latest Release](https://img.shields.io/pypi/v/imhist.svg)](https://pypi.org/project/imhist/)
[![Package Status](https://img.shields.io/pypi/status/imhist.svg)](https://pypi.org/project/imhist/)
[![Downloads](https://pepy.tech/badge/imhist)](https://pepy.tech/project/imhist)
[![License](https://img.shields.io/pypi/l/imhist.svg)](https://github.com/Mamdasn/imhist/blob/main/LICENSE)
![Repository Size](https://img.shields.io/github/languages/code-size/mamdasn/imhist)


# imhist  
This model calculates the histogram, PMF and CMD of a given image fast.  

## Installation

Run the following to install:

```python
pip install imhist
```

## Usage  
```python
import cv2
import numpy as np
from imhist import imhist, imcdf
import matplotlib.pyplot as plt

img = cv2.imread('assets/Plane.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
v = hsv[:, :, 2].copy()

v_hist = imhist(v)
v_pmf = imhist(v, PMF=True)
v_cdf = imcdf(v)

plt.figure(num=1)
plt.plot(np.arange(256), v_hist, 'b', label='Histogram')
plt.ylabel('Number of Occurrences')
plt.xlabel('Brightness')
plt.grid(which="both")
plt.legend()
plt.show()
```  
## Output
This is a sample image:  
![Sample Image](https://raw.githubusercontent.com/Mamdasn/imhist/main/assets/Plane.jpg "Sample Image")  
Histogram of the sample image:  
![Histogram of the Sample Image](https://raw.githubusercontent.com/Mamdasn/imhist/main/assets/Plane-Histogram.jpg "Histogram of the Sample Image")
