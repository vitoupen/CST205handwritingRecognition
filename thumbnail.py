from PIL import Image
from resizeimage import resizeimage

#im = Image.open("lion.jpg")
#im.show() #opens image app and displays photo
#print(im) #prints information and location
#print im.format, im.size, im.mode


fd_img = open('lion.jpg', 'r')
img = Image.open(fd_img)
img = resizeimage.resize_thumbnail(img, [200, 200])
img.save('test-lion.jpg', img.format)
fd_img.close()
