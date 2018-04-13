import csv
import cv2
import sys
import os
from PIL import Image,ImageDraw,ImageFont
#Aquiring information
f=open('Information.csv',"r")
lines=f.readlines()
format='jpg'
ld=340
xd=140
yd=885

l=620
xt=1225
xf=1935
xs=2640
xi=3350

xm1=1225
xm2=1950
xm3=2675
xm4=3405
xm5=4135

y1=405
y2=1400
y3=2405
for line in lines:
	info=line.split(',');
	partinfo=info[0];
	sysinfo=info[1];
	desc=info[2];
	desc=desc.split('\n')
	desc=desc[0]
	os.chdir('./'+partinfo);
	print os.getcwd();
	topo=cv2.imread('topo.'+format)
	fronto=cv2.imread('fronto.'+format)
	sideo=cv2.imread('sideo.'+format)
	isoo=cv2.imread('isoo.'+format)

	p1=cv2.imread('p1.'+format)
	p2=cv2.imread('p2.'+format)
	p3=cv2.imread('p3.'+format)
	p4=cv2.imread('p4.'+format)
	p5=cv2.imread('p5.'+format)

	topm=cv2.imread('topm.'+format)
	frontm=cv2.imread('frontm.'+format)
	sidem=cv2.imread('sidem.'+format)
	isom=cv2.imread('isom.'+format)
	var=0;
	if p4 is None:
		var=3;
		image=cv2.imread('../3.jpg');
	elif p5 is None:
		var=4;
		image=cv2.imread('../4.jpg');
	else:
		var=5;
		image=cv2.imread('../5.jpg');
	print var;

	p1 = cv2.resize(p1, (l,l))
	p2 = cv2.resize(p2, (l,l))
	p3 = cv2.resize(p3, (l,l))
	if var>3 :
		p4 = cv2.resize(p4, (l,l))
	if var>4 :
		p5 = cv2.resize(p5, (l,l))
	topo=cv2.resize(topo, (l,l))
	topm=cv2.resize(topm, (l,l))
	fronto=cv2.resize(fronto, (l,l))
	frontm=cv2.resize(frontm, (l,l))
	sideo=cv2.resize(sideo, (l,l))
	sidem=cv2.resize(sidem, (l,l))
	isoo=cv2.resize(isoo, (l,l))
	isom=cv2.resize(isom, (l,l))

	image[y1:y1+l,xt:xt+l]=topo[:,:]
	image[y1:y1+l,xf:xf+l]=fronto[:,:]
	image[y1:y1+l,xs:xs+l]=sideo[:,:]
	image[y1:y1+l,xi:xi+l]=isoo[:,:]

	image[y3:y3+l,xt:xt+l]=topm[:,:]
	image[y3:y3+l,xf:xf+l]=frontm[:,:]
	image[y3:y3+l,xs:xs+l]=sidem[:,:]
	image[y3:y3+l,xi:xi+l]=isom[:,:]

	image[y2:y2+l,xm1:xm1+l]=p1[:,:]
	image[y2:y2+l,xm2:xm2+l]=p2[:,:]
	image[y2:y2+l,xm3:xm3+l]=p3[:,:]
	if (var>3):
		image[y2:y2+l,xm4:xm4+l]=p4[:,:]
	if (var>4):
		image[y2:y2+l,xm5:xm5+l]=p5[:,:]
	cv2.imwrite('result.jpg',image)

	# Now for naming
	def splitlines(Description,width):
		array=[];
		line=''	
		words=Description.split()
		print words
		count=0;
		marker=0
		while marker<=len(words)-1 :
			while count<width and marker<=len(words)-1:
				print marker
				if len(words[marker])>width :
					marker+=1;
					break
				count+=len(words[marker]);
				marker+=1
			if marker== len(words) :
				array=array + [marker-1]
			else :
				array=array + [marker-1]
				marker=marker-1;		
			count=0;
		lines=[]
		count=0
		count2=0;
		markerlast=0;
		for marker in array:
			i=markerlast
			while i<=marker:		
				line=line+' '+words[i]
				i=i+1;
			lines=lines+ [line]
			line=''
			markerlast=i;
		return lines
		
	Part=(480,525)
	Sys=(585,625)
	point1=(150,890)
	point2=(960,1670)
	ROI=Image.new('RGB',(point2[0]-point1[0],point2[1]-point1[1]),"white")
	font=ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf',60,encoding="unic")
	draw=ImageDraw.Draw(ROI)
	import textwrap
	offset=0
	for line in splitlines(desc,10):
		print line+"!!!!!!"
		draw.text((0,offset),line,'black',font)
		offset+=font.getsize(line)[1]

	ROI.save("ROI.PNG","PNG")
	ROI=cv2.imread("ROI.PNG")
	image=cv2.imread("result.jpg")
	image[point1[1]:point2[1],point1[0]:point2[0]]=ROI[:,:]
	cv2.imwrite('result2.jpg',image)
	im=Image.open("result2.jpg")
	draw=ImageDraw.Draw(im)
	draw.text(Part,partinfo,'black',font)
	draw.text(Sys,sysinfo,'black',font)
	os.chdir("..")
	im.save(partinfo+".PNG","PNG")
