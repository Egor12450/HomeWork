# def setup():
#     size(600,600)
#     frameRate(1)
# def draw():
#     background(255)
#     for x in range(1,floor(random(10,200))):
#         stroke(random(0,255),random(0,255),random(0,255))
#         point(random(0,600),random(0,600))
#         strokeWeight(random(1,30))

y = 0
def setup():
    size(600,400)
    
def draw():
    global y
    background(100)
    translate(y,y)
    for x in range(20,300,20):
        rect(300,x,x,y)
    y = y + 1
