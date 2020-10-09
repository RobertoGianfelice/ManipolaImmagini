
def setup():
    global img
    img=createImage(100,100,RGB)
    size(600,400)
    
def draw():
    global img
    background(255,255,255)
    img.loadPixels()
    for x in range(100):
        for y in range(100):
            img.pixels[x+y*100]=color(x*256/100,y*256/100,0)
    img.updatePixels()
    image(img,mouseX,mouseY)
