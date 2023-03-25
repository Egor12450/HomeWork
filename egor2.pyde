x=[u"hello",u"egor",u"and",u"???"]
y=0
z=0
def setup():
    size(600,600)
def draw():
    if y > 3:
        y=0
    global z,y
    background(0)
    text(x[y],300,300)
    z=z+10
def keyPressed():
    global y
    if key == 'd':
        y=y+1
