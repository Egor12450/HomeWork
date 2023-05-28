x = []
y = []
h=0
def setup():
    size(600,400)
    strokeWeight(12)
    
def draw():
    global h
    background(100)
    for i in range(len(x)):
        translate(mouseX,mouseY)
        rotate(radians(h))
        ellipse(x[i],y[i],60,40)
    h=h+1
def mouseClicked():
    if mouseButton == LEFT:
        x.append(mouseX)
        y.append(mouseY)
    elif mouseButton == RIGHT:
        x.pop(len(x)-1)
        y.pop(len(y)-1)
