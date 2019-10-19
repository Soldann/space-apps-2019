from astropy.io import fits
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astropy.utils.data import get_pkg_data_filename
import os
import matplotlib.cm as cm
import subprocess
import glob

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
        "CK19Q040" : ["2019/" + str(i) for i in range(256, 293)]
        } # stores directory suffix where each objects pictures are stored

cwd = os.getcwd()
print(cwd)
def read_dirs(paths):
    images = []
    for path in paths:
        directory = "NEOSSAT/ASTRO/" + path + "/"
    return images

def generate_video(img):
    frames = [] # for storing the generated images
    fig = plt.figure()
    for i in range(len(img)):
        frames.append([plt.imshow(img[i], cmap=cm.Greys_r, animated=True)])
    
    ani = animation.ArtistAnimation(fig, frames, interval=250, blit=True,
                                   repeat_delay=1000)
    ani.save('movie.mov')
    plt.show()
    '''
    for i in range(len(img)):
        plt.imshow(img[i], cmap=cm.Greys_r)
        plt.savefig(cwd + "\\images\\file%02d.png" % i)

    subprocess.call([
        'ffmpeg', '-framerate', '8', '-i', 'file%02d.png', '-r', '30', '-pix_fmt', 'yuv420p',
        'video_name.mp4'
    ])
    os.system("ffmpeg -r 1 -i *.png -vcodec mpeg4 -y" + cwd + "movie.mp4")
    print("Done subprocess")
    for file_name in glob.glob("*.png"):
        os.remove(file_name)
    '''

generate_video(read_dirs(["2019/284"]))
print("Done!")
#image_file = get_pkg_data_filename('NEOSSAT/ASTRO/2019/284/NEOS_SCI_2019284114500.fits')
