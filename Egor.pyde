x=0
def setup():
    size(600,600)
def draw():
    global x
    img = loadImage("123.jpg")
    image(img,0,0,600,600)
    img = loadImage("1234.jpg")
    image(img,0,0,600,600)
    if x==2:
        x=0
    if keyPressed and key=="w":
        x=x+1
    if  x==0:
        img = loadImage("123.jpg")
        image(img,0,0,600,600)  
    if  x==1:
        img = loadImage("1234.jpg")
        image(img,0,0,600,600)  
