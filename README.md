# Photo_Sorter

This is a Python3-based image sorter with a graphical user interface. It uses the PIL library to extract the EXIF tags from each photo and identify the date the photo was taken. It is important to note that this program only works with JPEG photos. Through the GUI, the user can select the folder that contains the unsorted images and the folder that the sorted directories will be nested in. There is also the option to rename all of the photos based on the date they were taken. Having selected the proper folders and their renaming preference, the user simply clicks sort and the program takes care of the rest. I originally wrote this as a script to sort 10,000 images that I had accumulated and then turned it into a GUI based program streamline further use. In the future, I am going to implement a sort that ensures the photos are named chronologically within their folders so that photos taken in sequence are stored in the folder in sequence. I also intend to add the ability to select multiple folders to sort into one destination folder.

## Prerequisites for use:
- All images must be JPEGS
- The top level directory that will contain all image folders must already exist
- TKinter, Python3, and PIL must be installed on your machine
- Any photos that are the wrong format or missing date information will be placed in a folder named 00-0000.


**All photos in the folder selected as the starting folder will be re-sorted based on the date they were taken. Do not select a starting folder that contains photos sorted in any other way unless you would like them to be moved into new folders according to the time they were taken. It is okay if the destination folder already contains folders of photos regardless of how they are sorted. The photos in the destination folder will not be touched.**


As long as all of the prerequisits above are met, simply run the sorterGUI.py script, select the folder containing the photos and the folder you would like to be the sorted folders to be nested in. Check the box if you would like the photos to be renamed in a consistent format based on the date they were taken, and then hit sort. The photos will be moved into sub-folders in the destination folder and categorized as follows:

- Example image path after sorting: destinationFolder/Year/Month/Day/ImageName.JPEG
