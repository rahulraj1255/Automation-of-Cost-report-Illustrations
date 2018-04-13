import csv
import cv2
import sys
import os
from PIL import Image,ImageDraw,ImageFont
#Aquiring information
f=open('Information.csv',"r")
lines=f.readlines()
format='png'

# Text positions : Start from
PointTafull=(475,140)
PointTpfull=(1150,140)
PointTifull=(2035,140)

PointTahalf=(370,70)
PointTphalf=(1045,70)
PointTihalf=(1920,70)

PointTaonethird=(365,70)
PointTponethird=(1050,70)
PointTionethird=(1930,70)
#A3-----------------------------------------------------------------------------------
#Drawing
A3_Drawing_aspectratio=float(3065)/2085
A3_Drawing_dim=(2085,3065)
A3_Drawing_start=(205,245)
A3_Drawing_end=(2290,3310)
#Photo
A3_Photo_aspectratio=float(1900)/1405
A3_Photo_dim=(1405,1900)
A3_Photo_start=(200,300)
A3_Photo_end=(1605,2200)
#Processes
A3_Processes_aspectratio=float(815)/577
A3_Processes_dim=(577,815)
A3_Processes_1=(1708,310)
A3_Processes_2=(1708,1345)
A3_Processes_3=(1708,2410)
A3_Processes_4=(965,2410)
A3_Processes_5=(210,2410)

#A4 ---------------------------------------------------------------------------
#Drawing

A4_Drawing_aspectratio=float(1670)/2080
A4_Drawing_dim=(2080,1670)
A4_Drawing_start=(205,260)
A4_Drawing_end=(2285,1930)
#Photo
A4_Photo_aspectratio=float(260)/780
A4_Photo_dim=(780,1260)
A4_Photo_start=(205,2035)
A4_Photo_end=(985,3295)
#Processes
A4_Processes_aspectratio=float(535)/490
A4_Processes_dim=(490,535)

A4_Processes_1=(1095,2035)
A4_Processes_2=(1805,2035)
A4_Processes_3=(1805,2765)
A4_Processes_4=(1105,2765)

#A4_0.33 --------------------------------------------------------------------------
#Drawing
A4_33_Drawing_aspectratio=float(915)/1535
A4_33_Drawing_dim=(1535,915)
A4_33_Drawing_start=(105,175)
A4_33_Drawing_end=(1640,1090)
#Photo
A4_33_Photo_aspectratio=float(915)/690
A4_33_Photo_dim=(690,915)
A4_33_Photo_start=(1705,175)
A4_33_Photo_end=(2395,1090)

#A5  3 processes ------------------------------------------------------------------------------------
#Drawing
A5_3p_Drawing_aspectratio=float(910)/1530
A5_3p_Drawing_dim=(1530,910)
A5_3p_Drawing_start=(110,180)
A5_3p_Drawing_end=(1640,1090)
#Photo
A5_3p_Photo_aspectratio=float(925)/690
A5_3p_Photo_dim=(690,925)
A5_3p_Photo_start=(1705,170)
A5_3p_Photo_end=(2395,1095)
#Processes
A5_3p_Processes_aspectratio=float(480)/690
A5_3p_Processes_dim=(690,480)
A5_3p_Processes_1=(105,1160)
A5_3p_Processes_2=(910,1160)
A5_3p_Processes_3=(1710,1160)

#A5  4 processes ------------------------------------------------------------------------------------
#Drawing
A5_4p_Drawing_aspectratio=float(1030)/1430
A5_4p_Drawing_dim=(1430,1030)
A5_4p_Drawing_start=(105,175)
A5_4p_Drawing_end=(1535,1205)
#Photo
A5_4p_Photo_aspectratio=float(1035)/790
A5_4p_Photo_dim=(790,1035)
A5_4p_Photo_start=(1605,170)
A5_4p_Photo_end=(2395,1205)
#Processes
A5_4p_Processes_aspectratio=float(395)/495
A5_4p_Processes_dim=(495,395)

A5_4p_Processes_1=(105,1250)
A5_4p_Processes_2=(700,1255)
A5_4p_Processes_3=(1315,1255)
A5_4p_Processes_4=(1910,1255)
global imagep, imaged, image,p5,p4, var
def suitable_string(ImageType):
	if ImageType == "twopage":
		return "A3_"
	elif ImageType == "onepage":
			return "A4_"
	elif ImageType == "onethirdpage":
			return "A4_33_"
	else : # assuming it to be halfpage
		if var<4:
			return "A5_3p_"
			
		else :
			return "A5_4p_"

def crop(x,aspectratio):
	y1=x.shape[0];
	x1=x.shape[1];
	yr=aspectratio*x1;
	xr=y1/aspectratio;
	if xr<x1:
		x=x[:,int((x1-xr)/2):x1-int((x1-xr)/2)];
	else:
		x=x[int((y1-yr)/2):y1-int((y1-yr)/2),:];
	return x

		
for line in lines:
	info=line.split(',');
	Assembly_Name=info[0];
	Part_Name=info[1];
	Part_Id=info[2];
	ImageType=info[3];
	ImageType=ImageType.split('\n')
	ImageType=ImageType[0]

	os.chdir('./'+Part_Name);
	print os.getcwd();
	drawing=cv2.imread('draw.'+format)
	photo=cv2.imread('photo.'+format)
	p1=cv2.imread('p1.'+format)
	p2=cv2.imread('p2.'+format)
	p3=cv2.imread('p3.'+format)
	p4=cv2.imread('p4.'+format)
	p5=cv2.imread('p5.'+format)
	
	if p3 is None:
		var=0
	elif p4 is None :
		var=3
	elif p5 is None :
		var=4
	else:
		var=5;
		
	ImageString=suitable_string(ImageType)
	drawing=crop(drawing,globals()[ImageString+"Drawing_aspectratio"])
	photo=crop(photo,globals()[ImageString+"Photo_aspectratio"])
	try:
		p1=crop(p1,globals()[ImageString+"Processes_aspectratio"])
	except:
		pass
	try:
		p2=crop(p2,globals()[ImageString+"Processes_aspectratio"])
	except:
		pass
	try:
		p3=crop(p3,globals()[ImageString+"Processes_aspectratio"])
	except:
		pass
	try:
		p4=crop(p4,globals()[ImageString+"Processes_aspectratio"])
	except:
		pass
	try:
		p5=crop(p5,globals()[ImageString+"Processes_aspectratio"])
	except:
		pass
	if ImageType == 'twopage':
		imaged=cv2.imread('../a3-drawing.png');
		imagep=cv2.imread('../a3-photo.png');
	elif ImageType == 'onepage':
		image=cv2.imread('../a4.png');
	elif ImageType == 'halfpage':
		if p4 is None:  
			image=cv2.imread('../a5-3process.png')
		else:
			image=cv2.imread('../a5-4process.png')
	else:					#Assuming it to be onethird page
		image=cv2.imread('../a4-0.33.png');

		
	if var!=0 :
		p1 = cv2.resize(p1, globals()[ImageString+"Processes_dim"])
		p2 = cv2.resize(p2, globals()[ImageString+"Processes_dim"])
		p3 = cv2.resize(p3, globals()[ImageString+"Processes_dim"])
	if var>3 :
		p4 = cv2.resize(p4, globals()[ImageString+"Processes_dim"])
	if var>4 :
		p5 = cv2.resize(p5, globals()[ImageString+"Processes_dim"])
	drawing=cv2.resize(drawing, globals()[ImageString+"Drawing_dim"])
	photo=cv2.resize(photo, globals()[ImageString+"Photo_dim"])
	
	if ImageType != "twopage" :
		Start=globals()[ImageString+"Drawing_start"]
		End=globals()[ImageString+"Drawing_end"]
		image[Start[1]:End[1],Start[0]:End[0]]=drawing[:,:]
		Start=globals()[ImageString+"Photo_start"]
		End=globals()[ImageString+"Photo_end"]
		image[Start[1]:End[1],Start[0]:End[0]]=photo[:,:]
		
		if var!=0 :
			Start=globals()[ImageString+"Processes_1"]
			Dim=globals()[ImageString+"Processes_dim"]
			image[Start[1]:Start[1]+Dim[1],Start[0]:Start[0]+Dim[0]]=p1[:,:]	
			Start=globals()[ImageString+"Processes_2"]
			image[Start[1]:Start[1]+Dim[1],Start[0]:Start[0]+Dim[0]]=p2[:,:]	
			Start=globals()[ImageString+"Processes_3"]
			image[Start[1]:Start[1]+Dim[1],Start[0]:Start[0]+Dim[0]]=p3[:,:]
		if var>3 :
			Start=globals()[ImageString+"Processes_4"]
			image[Start[1]:Start[1]+Dim[1],Start[0]:Start[0]+Dim[0]]=p4[:,:]
		if var>4:
			Start=globals()[ImageString+"Processes_5"]
			image[Start[1]:Start[1]+Dim[1],Start[0]:Start[0]+Dim[0]]=p5[:,:]
	else:
		Start=globals()[ImageString+"Photo_start"]
		End=globals()[ImageString+"Photo_end"]
		imagep[Start[1]:End[1],Start[0]:End[0]]=photo[:,:]
		Start=globals()[ImageString+"Drawing_start"]
		End=globals()[ImageString+"Drawing_end"]
		imaged[Start[1]:End[1],Start[0]:End[0]]=drawing[:,:]
		Start=globals()[ImageString+"Processes_1"]
		Dim=globals()[ImageString+"Processes_dim"]
		imagep[Start[1]:Start[1]+Dim[1],Start[0]:Start[0]+Dim[0]]=p1[:,:]	
		Start=globals()[ImageString+"Processes_2"]
		imagep[Start[1]:Start[1]+Dim[1],Start[0]:Start[0]+Dim[0]]=p2[:,:]	
		Start=globals()[ImageString+"Processes_3"]
		imagep[Start[1]:Start[1]+Dim[1],Start[0]:Start[0]+Dim[0]]=p3[:,:]
		Start=globals()[ImageString+"Processes_4"]
		imagep[Start[1]:Start[1]+Dim[1],Start[0]:Start[0]+Dim[0]]=p4[:,:]
		Start=globals()[ImageString+"Processes_5"]
		imagep[Start[1]:Start[1]+Dim[1],Start[0]:Start[0]+Dim[0]]=p5[:,:]
	if ImageType!="twopage":
		cv2.imwrite('result.jpg',image)
	else:
		cv2.imwrite('resultd.jpg',imaged)
		cv2.imwrite('resultp.jpg',imagep)

# Now for naming
	font=ImageFont.truetype('../OpenSans-Regular.ttf',60,encoding="unic")
	if ImageType=="onethirdpage":
		im=Image.open("result.jpg")
		draw=ImageDraw.Draw(im)
		draw.text(PointTaonethird,Assembly_Name,'black',font)
		draw.text(PointTponethird,Part_Name,'black',font)
		draw.text(PointTionethird,Part_Id,'black',font)
		os.chdir("..")
		im.save(Part_Name+".PNG","PNG")
	elif ImageType=="halfpage":
		im=Image.open("result.jpg")
		draw=ImageDraw.Draw(im)
		draw.text(PointTahalf,Assembly_Name,'black',font)
		draw.text(PointTphalf,Part_Name,'black',font)
		draw.text(PointTihalf,Part_Id,'black',font)
		os.chdir("..")
		im.save(Part_Name+".PNG","PNG")
	elif ImageType=="onepage":
		im=Image.open("result.jpg")
		draw=ImageDraw.Draw(im)
		draw.text(PointTafull,Assembly_Name,'black',font)
		draw.text(PointTpfull,Part_Name,'black',font)
		draw.text(PointTifull,Part_Id,'black',font)
		os.chdir("..")
		im.save(Part_Name+".PNG","PNG")
	else:
		imd=Image.open("resultd.jpg")
		draw=ImageDraw.Draw(imd)
		draw.text(PointTafull,Assembly_Name,'black',font)
		draw.text(PointTpfull,Part_Name,'black',font)
		draw.text(PointTifull,Part_Id,'black',font)
		imp=Image.open("resultp.jpg")
		draw2=ImageDraw.Draw(imp)
		draw2.text(PointTafull,Assembly_Name,'black',font)
		draw2.text(PointTpfull,Part_Name,'black',font)
		draw2.text(PointTifull,Part_Id,'black',font)
		os.chdir("..")
		imd.save(Part_Name+"_Drawing"+".PNG","PNG")
		imp.save(Part_Name+"_Photo"+".PNG","PNG")
