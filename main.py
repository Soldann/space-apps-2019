from astropy.io import fits
import cv2

img = fits.open('NEOSSAT/ASTRO/2019/284/NEOS_SCI_2019284114500.fits')
print("Hello world")
cv2.imshow('image',img[0].data)


img.close()
