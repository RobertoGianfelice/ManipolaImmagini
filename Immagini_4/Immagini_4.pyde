size(1024,1024)
frog=loadImage("frog.jpg")
frog.loadPixels()
img=createImage(frog.width,frog.height,RGB)
img.loadPixels()

loadPixels()

for x in range(frog.width*frog.height):
    r=red(frog.pixels[x])
    g=green(frog.pixels[x])
    b=blue(frog.pixels[x])
    img.pixels[frog.width*frog.height-x-1]=color(r,g,b)
img.updatePixels()
image(img,0,0)
