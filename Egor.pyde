import time
x=0
y=0
z=0
def setup():
    size(600,600)
def draw():
    global x,y,z
    img = loadImage("123.jpg")
    image(img,0,0,600,600)
    img = loadImage("1234.jpg")
    image(img,0,0,600,600)
    if x==3:
        x=0
    if keyPressed and key=="n":
        x=x+1
        time.sleep(2)
    if  x==0:
        img = loadImage("123.jpg")
        image(img,0,0,600,600)  
    if  x==1:
        img = loadImage("1234.jpg")
        image(img,0,0,600,600)  
    if  x==2:
        img = loadImage("12345.jpg")
        image(img,0,0,600,600)
    translate(z,y)
    fill(0)
    if keyPressed and key=="f": 
        fill(random(0,255),random(0,255),random(0,255))
    strokeWeight(5)
    ellipse(300,300,50,100)
    ellipse(300,250,50,50)
    line(300,300,350,300)
    line(300,300,250,300)
    line(300,300,350,370)
    line(300,300,250,370)
    if keyPressed and key=="w": 
        y=y-10
    if keyPressed and key=="s": 
        y=y+10
    if keyPressed and key=="a": 
        z=z-10
    if keyPressed and key=="d": 
        z=z+10
    if keyPressed and key=="0": 
        y=0
        z=0
