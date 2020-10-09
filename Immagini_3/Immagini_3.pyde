
def setup():
    global frog
    size(1024,560)
    frog=loadImage("frog2.jpg")
    frog.loadPixels()
    loadPixels()



def draw():
    car=0
    bit=15
    for x in range(width):
        for y in range(height):
            loc=x+y*width
            r=red(frog.pixels[loc])
            g=green(frog.pixels[loc])
            b=blue(frog.pixels[loc])
            dis=dist(mouseX,mouseY,x,y)
            factor=map(dis,0,200,2,0)
            factor=max(factor,0)
            pixels[loc]=color(r*factor,g*factor,b*factor)
    updatePixels()
