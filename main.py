from astropy.io import fits

img = fits.open('NEOSSAT/ASTRO/2019/284/NEOS_SCI_2019284114500.fits')

print("Hello world")


img.close()
