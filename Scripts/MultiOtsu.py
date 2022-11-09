import numpy as np
import sys
from skimage.filters import threshold_multiotsu

image_path = sys.argv[1]
N = int(sys.argv[2])

volume = open(image_path,"rb")
volume = np.fromfile(volume, dtype=np.uint8).reshape([N,N,N])

thr_multiotsu = threshold_multiotsu(volume)
binary = volume >= thr_multiotsu[0]

porosity = 1-np.mean(binary)

print('Computed Sample Porosity {}'.format(porosity))

binary.tofile(image_path.replace('.raw', '') +'-normalized-MultilevelOtsu.raw')
      
print('Image saved to: {}'.format(image_path.replace('.raw', '') +'-normalized-MultilevelOtsu.raw'))