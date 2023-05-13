def setup():
    size(600,600)
def draw():
    strokeWeight(0)
    def snegovik(x,y,z,c):
        fill(c)
        ellipse(0+x,-45+y,30+z,30+z)
        ellipse(0+x,0+y,60+z,60+z)
        ellipse(0+x,75+y,90+z,90+z)
        line(0+x,0+y,70+y,0+y)
        line(0+x,0+y,-70+y,0+y)
    snegovik(200,200,10,255)
    snegovik(300,300,0,200)
