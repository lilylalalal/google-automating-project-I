import os,sys
from PIL import Image

#src= 'c/Users/lawmi/Desktop/PY3/google_py3/imgfile/images'

def modifypic(pic,directory):
    image=Image.open(directory+"/"+pic)
    #newpic = pic.replace("tiff", "jpeg")
    im=image.convert('RGB')
    new = im.rotate(90).resize((128,128))
    return new.save("/opt/icons/"+"resized"+pic +'.jpeg')

def picinfolder(directory):
    file = os.listdir(directory)
    for pic in file:
        newpic = modifypic(pic,directory)
    return newpic

if __name__ == "__main__":
    picinfolder("imgfile/images")
