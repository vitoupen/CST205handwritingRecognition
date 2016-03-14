from PIL import Image
from resizeimage import resizeimage

#OPEN THE LION PICTURE, STORE IN im
kovu = Image.open("lion.jpg")

#OPENS IMAGE APP AND DISPLAYS PHOTO
kovu.show()

#PRINTS INFORMATION AND LOCATION 
print(kovu)
print kovu.format, kovu.size, kovu.mode
