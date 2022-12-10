x=0
def setup():
    size(600,600)
def draw():
    rect(50,300,100,100)
    rect(450,300,100,100)
    rect(250,300,100,100)
    random(1,3)
def mouseClicked():   
        if mouseX > 50 and mouseX < 150 and mouseY > 300 and mouseY < 400:
            img=loadImage("rr.jpg")
            image(img,50,300,100,100)
            noLoop()
    
        if mouseX > 450 and mouseX < 550 and mouseY > 300 and mouseY < 400:
            img=loadImage("cc.jpg")
            image(img,450,300,100,100)
            noLoop()
    
        if mouseX > 250 and mouseX < 350 and mouseY > 300 and mouseY < 400:
            img=loadImage("cc.jpg")
            image(img,250,300,100,100)
            noLoop()   
