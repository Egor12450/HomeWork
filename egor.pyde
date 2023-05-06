x = []
y = []
def setup():
    size(600,600)
    strokeWeight(5)
def draw():
    background(255)
    global x,y
    for i in range(len(x)):
        point(x[i],y[i])
def mouseClicked():
    global x,y
    if mouseButton==LEFT:
        point(mouseX,mouseY)
        x.append(mouseX)
        y.append(mouseY)
    if mouseButton==RIGHT:
        x.pop(len(x)-1)
        y.pop(len(y)-1)
