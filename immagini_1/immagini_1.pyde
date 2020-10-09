
def setup():
    global img
    size(600,400)
    img=loadImage("LogoScuola.png")
    
def draw():
    background(0,0,0)
    image(img,mouseX,mouseY)
    
    
