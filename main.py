from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.utils.data import get_pkg_data_filename
import os
import matplotlib.cm as cm
import subprocess
import glob

cwd = os.getcwd()

def read_dirs(year, numbers):
    images = []
    for number in numbers:
        directory = "NEOSSAT/ASTRO/" + str(year) +"/" + str(number) + "/"
    
        for filename in os.listdir(directory):
            if filename.endswith("clean.fits"): 
                image_file = get_pkg_data_filename(directory + filename)
                image_data = fits.getdata(image_file, ext=0)
                images.append(image_data)
                ''' 
                plt.figure()
                plt.imshow(image_data, cmap='gray')
                plt.colorbar()
                print(filename)
                '''
                #plt.close()
    return images
def generate_video(img):
    for i in range(len(img)):
        plt.imshow(img[i], cmap=cm.Greys_r)
        plt.savefig(cwd + "/file%02d.png" % i)

    '''subprocess.call([
        'ffmpeg', '-framerate', '8', '-i', 'file%02d.png', '-r', '30', '-pix_fmt', 'yuv420p',
        'video_name.mp4'
    ])'''
    os.system("ffmpeg -r 1 -i file%01d.png -vcodec mpeg4 -y movie.mp4")
    print("Done subprocess")
    for file_name in glob.glob("*.png"):
        os.remove(file_name)
        

generate_video(read_dirs(2019, [284]))
print("Done!")
#image_file = get_pkg_data_filename('NEOSSAT/ASTRO/2019/284/NEOS_SCI_2019284114500.fits')
