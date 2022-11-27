# size(400,600)
# textSize(20)
# fill(255) #да, и цвет текста это задаёт тоже
# textAlign(LEFT,TOP) # а так же LEFT/RIGHT и TOP/BOTTOM
# text(u"Привет",200,300) # u чтоб кракозябры вместо русских букв не писались
# point(200,300)

# x=0
# def setup():
#     size(600,600)
# def draw():
#     global x
#     rect(300,300,50,50)
#     text(u"счет",100,100)
# def mouseClicked():
#     global x
#     if mouseX > 300 and mouseX < 350 and mouseY > 300 and mouseY < 350:
#         x=x+1
#     textSize(20)
#     background(255)
#     fill(0,0,255)
#     text(x,150,100)

# def setup():
#      size(600,600)
# def draw():
#     if mousePressed:
#         background(255)
#         fill(0,0,255)
#         rect(mouseX,mouseY,50,50)

x=1
def setup():
    size(600,600)

def draw():
    
    global x
    strokeWeight(5)
    rect(200,500,100,50)
    rect(400,500,100,50)
    rect(50,500,100,50)
    if mousePressed == True:
        strokeWeight(x)
        point(mouseX,mouseY)
        
def mouseClicked():
    global x
    if mouseX > 200 and mouseX < 300 and mouseY > 500 and mouseY < 550:
        x=x+1
    if mouseX > 400 and mouseX < 500 and mouseY > 500 and mouseY < 550:
        x=x-1
    if mouseX > 50 and mouseX < 150 and mouseY > 500 and mouseY < 550:
        background(255)
        # rect(0,0,600,600)
        # rect(200,500,100,50)
        # rect(400,500,100,50)
        # rect(50,500,100,50)
