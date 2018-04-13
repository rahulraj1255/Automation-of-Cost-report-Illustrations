# Automation-of-Cost-report-Illustrations
Introduction:
This tool (python script) simplifies the process of inserting photos and text in cost report illustration templates. For image manipulations it uses OpenCV and PIL libraries for python. 

Added functionality of auto-cropping : The assumption of images being of proper aspect ratio is dropped now. The code automatically converts it to an aspect ratio which exactly suites the box where it is to be placed. The new cropped image is an image of maximum area (and of desired aspect ratio) which can be placed on the original image (centre of both the images are coincident). In other words, the length or the breadth of original image will be reduced equally from both sides so as to make the new aspect ratio equal to the desired aspect ratio.

Prerequisites:
A linux distribution : Preferably Ubuntu
Install some packages from the terminal
sudo apt-get install libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
(In my case libjpeg installation was showing an error, so just remove it from the line and try again)        
Install PIL for python
pip install PIL (if pip is not installed, install it by easy_install pip)
OpenCV
pip install cv2    
Instructions for use:
Required Organisation of folder:
The folder should contain various folders named after each part (partname). Each folder containing the images to be placed on its illustration.
The naming of the images is as follows:
draw.png : for drawing of the part
photo.png : for actual photo of the part in isometric view
p1.png, p2.png, p3.png,... : images of the part at various process stages (For two page, one page, onethirdpage the number of these images should be is per the template, for half page it could either contain 3 processes or 4 processes {the script automatically picks up the right template depending upon the number of images present})
The folder should also contain a csv file containing the text information:
Fields : Assembly, Part name, part Id, type of illustration to be used (onepage, twopage, onethirdpage, halfpage)
Should not contain headings, just start writing the field values from the first row itself.
This csv file should be named as “Information.csv”
Process templates named as follows:
“a5-4process.png” for 4 process halfpage layout
“a5-3process.png” for 3 process halfpage layout
“A4.png” for onepage layout
“a4-0.33.png” for onethirdpage layout
“a3-photo.png” template containing photo and processes for twopage layout
“a3-drawing.png” template containing drawing for twopage layout
“OpenSans-Regular.ttf” font should also be present in the same folder. This is the font which is being used for texts in illustration.
Executing the code:
Make sure you are in the same folder as described in part (1)
Make the script executable
chmod a+x script.py
Execute the script
python script.py
Output
The folder should now contain all the generated illustration named as follows:
Two page illustrations are named as partname_Drawing.PNG and partname_Photo.PNG.
Other illustrations are named as partname.PNG.
A sample folder with ordered images and files is uploaded on drive for reference. Also note that it contains the generated images.
