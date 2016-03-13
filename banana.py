def getSquare(im):
    from PIL import Image
    
    im = im.crop(getBox(im))
    return im
    
def getBox(im):
 width = im.width
 height = im.height
 pix = im.load()
	
 xmin = width
 xmax = 0
 ymin = height
 ymax = 0
    
 for w in range(0, width):
  for h in range(0, height):
   pixel = pix[w,h]
   if (pixel[0] < 255 or pixel[1] < 255 or pixel[2] < 255):
    if (w > xmax): xmax = w
    if (w < xmin): xmin = w
    if (h > ymax): ymax = h
    if (h < ymin): ymin = h

 #return xmin, ymin, xmax, ymax
 return getBoxDims(xmin, xmax, ymin, ymax)
 
def getBoxDims(xmin, xmax, ymin, ymax):
    dx = xmax - xmin
    dy = ymax - ymin
    
    if (dx > dy):
        difference = dx - dy
        half1 = difference / 2
        half2 = difference - half1
        ymin -= half1
        ymax += half2
    elif (dy > dx):
        difference = dy - dx
        half1 = difference / 2
        half2 = difference - half1
        xmin -= half1
        xmax += half2

    return xmin, ymin, xmax, ymax