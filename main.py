from astropy.io import fits
import cv2
import matplotlib.pyplot as plt
from astropy.utils.data import get_pkg_data_filename
import os

timelapse = {
        "2018-RC": ["2018/250"], 
        "46P" : ["2018/281", "2018/284", "2018/285", "2018/290", "2018/293", "2018/300", "2018/319", "2018/321", "2018/335", "2018/345", "2018/348", "2018/349"],
        "J12192806" : ["2018/314"],
        "C2018-V1" : ["2018/321"],
        "2018-KV" : ["2018/335"],
        "64P" : ["2018/345"],
        "P10KLoS" : ["2019/004"],
        "2019-AQ3" : ["2019/040"],
        "2019-EA2" : ["2019/075", "2019/081"],
        "1999-KW4" : ["2019/118","2019/119","2019/120","2019/121","2019/122","2019/123","2019/124","2019/124","2019/125","2019/126","2019/128","2019/129","2019/130","2019/131","2019/132","2019/133","2019/134","2019/135","2019/136","2019/137","2019/138","2019/139","2019/140","2019/141","2019/142","2019/143","2019/144","2019/145","2019/146","2019/147","2019/148","2019/149","2019/150","2019/151","2019/152"],
        "2019-A10dn4M" : ["2019/124"],
        "CK19D010" : ["2019/128"],
        "A10dQbl" : ["2019/150"],
        "A10dRr5" : ["2019/150"],
        "2019-K1" : ["2019/243","2019/244"],
        "2019-A9" : ["2019/243","2019/244"],
        "2019-W1" : ["2019/243","2019/244"],
        "2018-F4" : ["2019/243","2019/244"],
        "2017-T2" : ["2019/243","2019/244"],
        "2019-K5" : ["2019/243","2019/244"],
        "CK19Q040" : ["2019/" + str(i) for i in range(256, 292)]
        } # stores directory suffix where each objects pictures are stored

print(timelapse["CK19Q040"])
img = fits.open('NEOSSAT/ASTRO/2019/284/NEOS_SCI_2019284114500.fits')
cv2.imshow('image',img[0].data)
cv2.waitKey(0)
cv2.destroyAllWindows()

img.close()

directory = "NEOSSAT/ASTRO/2019/284/"

for filename in os.listdir(directory):
    if filename.endswith("clean.fits"): 
        image_file = get_pkg_data_filename(directory  + filename)
        image_data = fits.getdata(image_file, ext=0)
        plt.figure()
        plt.imshow(image_data, cmap='gray')
        plt.colorbar()
        print(filename)
        plt.close()

