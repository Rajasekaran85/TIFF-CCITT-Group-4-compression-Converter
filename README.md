# Application Title

TIFF Image CCITT Group 4 compression Converter

## Description

* Convert the Black & White Images to CCITT Group 4 compression
* pillow library used
* wand (imagemagick) library used
* Images types: TIF

## Getting Started

### Dependencies

* Windows 7

### Installing

* pip install Pillow
* pip install wand

### Executing program

* Run the program
* Ask user to enter the path of the input image file
* Tool will create the Folder "Group4" in the same directory of input file
* Group4 compression apply only for Black & White mode images.
* So tool should check the images, it is present in Black & White mode and then convert to Group4 compression
* If any of the images not present in "Black & White" mode and already image in "Group4" compression, then those file list will write in the log file "output.log".
* The converted Image files will placed in the "Group4" folder


## Version History

* 0.1
    * Initial Release
