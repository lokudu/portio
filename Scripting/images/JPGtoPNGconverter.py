import sys
import os
from PIL import Image

#grab first and second arguement

image_folder = sys.argv[1]
output_folder = sys.argv[2]

#print(images, new)
#check is new/ exist or if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
#loop through images
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')

#convert images to png
#save images to new folder

#if __name__ == '__main__':
    #print(sys.argv)