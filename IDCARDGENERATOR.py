from PIL import Image,ImageDraw,ImageFont #importing  libraries

#creating an image
img = Image.new('RGB',(350,200),color = 'white')


vk = Image.open("download.jpg").convert('RGBA')
img.paste(vk,(100,40),vk)

#Initialising a Font
fnt = ImageFont.truetype("arial.ttf",14) 

#passing img to the Draw method
d = ImageDraw.Draw(img)




#Displaying Name Field
d.text((20,50),"NAME:",font = fnt,fill=(0,0,0,0))
#Taking Name from user
name =  input("Enter Your Name:")
#Pasting name to the Image
d.text((70,50),name,font = fnt,fill=(0,0,0,0))

#Displaying BRANCH Field
d.text((20,80),"BRANCH:",font = fnt,fill=(0,0,0,0))
#Taking BRACH from user
branch =  input("Enter Your Branch:")
#Pasting BRANCH to the Image
d.text((85,80),branch,font = fnt,fill=(0,0,0,0))

#Displaying IDNO Field
d.text((20,110),"ID NO:",font = fnt,fill=(0,0,0,0))
import random
y=random.randint(15,19)
no=random.randint(1,99)
if(branch=="CSE" or "cse"):
    b=5
elif(branch=="ECE" or "ece"):
    b=4
elif(branch=="EEE" or "eee"):
    b=3
elif(branch=="MECH" or "mech"):
    b=2
if(no == 1 or no == 2 or no == 3 or no == 4 or no == 5 or no == 6 or no == 7 or no == 8 or no == 9):
    f=0
    d.text((70,110),"{}KD1A0{}{}{}".format(y,b,f,no),font = fnt,fill=(0,0,0,0))
else:
    d.text((70,110),"{}KD1A0{}{}".format(y,b,no),font = fnt,fill=(0,0,0,0))

#Displaying DOB Field
d.text((20,140),"D.O.B:",font = fnt,fill=(0,0,0,0))
#Taking DOB from user
dob =  input("Enter Your D.O.B:")
#Pasting DOB to the Image
d.text((70,140),dob,font = fnt,fill=(0,0,0,0))







#Displaying PHNO Field
d.text((20,170),"PH NO:",font = fnt,fill=(0,0,0,0))
#Taking PHNO from user
phno =  input("Enter Your Phone Number:")
#Pasting PHNO to the Image
d.text((70,170),phno,font = fnt,fill=(0,0,0,0))






import cv2

image = cv2.imread("vasanth.jpg",1)

resized = cv2.resize(image,(int(image.shape[1]/22),int(image.shape[1]/22)))

cv2.imwrite("vasanth1.jpg",resized)

try:
    resized1 = Image.open("vasanth1.jpg")
    img.paste(resized1,(240,50))
except IOError:
    pass


try:
    img2 = Image.open("images.png")
    img.paste(img2,(0,0))
except IOError:
    pass



import qrcode

# Create qr code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size =1.5,
    border = 0,
)

# The data that you want to store
data = "The Data that you need to store in the QR Code"

# Add data
qr.add_data(name)
qr.add_data(dob)
qr.add_data(branch)
qr.add_data(phno)
qr.add_data("{}KD1A0{}{}".format(y,b,no))
qr.make(fit=True)

# Create an image from the QR Code instance
img3 = qr.make_image()


try:
    img.paste(img3,(275,140))
except IOError:
    pass



img.save("First.png")


