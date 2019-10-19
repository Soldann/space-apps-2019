from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.utils.data import get_pkg_data_filename
import os


def read_dirs(year, numbers):
    for number in numbers:
        directory = "NEOSSAT/ASTRO/" + year +"/" + number
    
        for filename in os.listdir(directory):
            if filename.endswith("clean.fits"): 
                image_file = get_pkg_data_filename(directory  + filename)
                image_data = fits.getdata(image_file, ext=0)
                plt.figure()
                plt.imshow(image_data, cmap='gray')
                plt.colorbar()
                print(filename)
                #plt.close()

#image_file = get_pkg_data_filename('NEOSSAT/ASTRO/2019/284/NEOS_SCI_2019284114500.fits')
