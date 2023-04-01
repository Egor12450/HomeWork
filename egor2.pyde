def setup():
    size(600,600)
def draw():
    i=["ellipse","rect","triangle","rect","ellipse"]
    for x in range(len(i)):
        if i[x]=="ellipse":
            ellipse(300,100,50,50)
        if i[x]=="rect":
            rect(300,100,50,50)
        if i[x]=="triangle":
            triangle(300,100,350,150,250,150)
        translate(0,100)
