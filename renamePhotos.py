from PIL import Image
from PIL.ExifTags import TAGS
from os import listdir, walk, rename
import tkinter
from tkinter.filedialog import askdirectory




def extractDate(image):
        imageInfo = {}
        openImage = Image.open(image)
        exifdata = openImage.getexif()
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            imageInfo[tag] = data
        date = imageInfo['DateTimeOriginal']
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        return year, month, day



def renamePhotos(dPath):
    i = 1
    photos = listdir(dPath)
    for filename in photos:
        filePath = dPath+'/'+filename
        try:
                year, month, day = extractDate(filePath)
                newName = '{0}-{1}-{2}-{3}'.format(year, month, day, i)
                rename(filePath, dPath+'/'+newName+'.jpg')
                i+=1
        except:
                continue

def main():
    tkinter.Tk().withdraw()
    dPath = askdirectory()
    renamePhotos(dPath)

if __name__ == '__main__':
    main()
