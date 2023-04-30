import time
x=0
y=0
z=0
mode = 0
def setup():
    size(600,600)
def draw():
    global x,y,z, mode

    if x==3:
        x=0
    if keyPressed and key=="n":
        x=x+1
        time.sleep(2)
    if x==0:
        img = loadImage("123.png")
        image(img,0,0,600,600)  
    if  x==1:
        img = loadImage("1234.png")
        image(img,0,0,600,600)  
    if  x==2:
        img = loadImage("12345.png")
        image(img,0,0,600,600)
    translate(z,y)
    fill(0)
    if keyPressed and key=="f": 
        fill(random(0,255),random(0,255),random(0,255))
    strokeWeight(5)
    if mode == 1:
        ellipse(400,300,50,100)
        ellipse(400,250,50,50)
        line(400,300,450,300)
        line(400,300,350,300)
        line(400,300,450,370)
        line(400,300,350,370)
        line(400,300,400,250)
    ellipse(300,300,50,100)
    ellipse(300,250,50,50)
    line(300,300,350,300)
    line(300,300,250,300)
    line(300,300,350,370)
    line(300,300,250,370)
    line(300,300,300,250)
    line(400,250,300,250)
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
    if keyPressed and key=="1": 
        mode = 1
    if keyPressed and key=="2": 
        mode = 0
    if y>240:
        y=240
    if y<-230:
        y=-230
    if z<-250:
        z=-250
    if z>150:
        z=150
    print(z)
