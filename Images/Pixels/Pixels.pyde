size(800,600)

# for i in range(width):
#     set(i,200,color(255,0,0))
#     print (get(i,200))

#loadPixels()
#for i in range(len(pixels)):
#    pixels[i]=color(254,0,0)
#updatePixels()

loadPixels()
for x in range(width):
    for y in range(height):
        pixels[x+y*width]=color(x*256/width,y*256/height,0)
updatePixels()

    
