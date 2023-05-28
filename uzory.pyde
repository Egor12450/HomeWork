import random
x = []
y = []
z = []
h = []
def setup():
    size(600,400)
    strokeWeight(12)
    
def draw():
    global h
    background(100)
    for i in range(len(x)):
        push()
        translate(x[i],y[i])
        rotate(radians(h[i]))
        ellipse(0,0,60,40)
        rect(10,10,60,40)
        rect(-70,10,60,40)
        pop()
        h[i]=h[i]+z[i]
    # h=h+1
def mouseClicked():
    if mouseButton == LEFT:
        x.append(mouseX)
        y.append(mouseY)
        h.append(0)
        z.append(random.choice([-2, -1, 1, 2]))
    elif mouseButton == RIGHT:
        if len(x)>0:
            x.pop(len(x)-1)
        if len(y)>0:
            y.pop(len(y)-1)
        if len(z)>0:
            z.pop(len(z)-1)
        if len(h)>0:
            h.pop(len(h)-1)
