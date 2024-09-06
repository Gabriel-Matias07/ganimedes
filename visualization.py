from astropy.io import fits
import matplotlib.pyplot as plt

hdulist = fits.open('Maps/HERSCHEL/anonymous1725578900/hpacs1342220557_20hpppmapb_00_1469433805960.fits')

image_data = hdulist[2].data  

plt.imshow(image_data, cmap='gray')
plt.colorbar()
plt.show()
