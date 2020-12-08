from PIL import Image
from PIL.ExifTags import TAGS
from os import walk, rename, mkdir, listdir, rmdir
from renamePhotos import *

def extractDate(image):
    try:
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
    except KeyError:
        return '0000', '00', '00'
    
    
def sortPhotos(sPath, dPath, renaming):
    photos = []
    folders = listdir(dPath)
    if renaming == 0:
        renamePhotos(sPath)
    for (dirpath, dirname, filename) in walk(sPath):
        photos.extend(filename)
        folders.extend(dirname)
    for filename in photos:
        try:
            pPath = sPath+'/'+filename
            year, month, day = extractDate(pPath)
            fName = month+'-'+year
            cfName = month+'-'+day+'-'+year
            if fName not in folders:
                folders.append(fName)
                mkdir(dPath+'/'+fName)
            if cfName not in folders:
                folders.append(cfName)
                mkdir(dPath+'/'+fName+'/'+cfName)
            rename(pPath, "{0}/{1}/{2}/{3}".format(dPath, fName, cfName, filename))
        except:
            continue

