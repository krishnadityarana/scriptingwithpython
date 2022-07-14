import sys
import os
from PIL import Image

grabedimage = sys.argv[1]
convertedimage = sys.argv[2]

if not os.path.exists(convertedimage):
    (os.mkdir(convertedimage))

for i in os.listdir(grabedimage):
    img = Image.open(f'{grabedimage}{i}')
    clean_name = os.path.splitext(i)[0]
    img.save(f'{convertedimage}{clean_name}.jpg')
    print('all done!')


