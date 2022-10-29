# x=0
# def setup():
#     size(600,600)

# def draw():
#     global x
#     translate(300,300)
#     rotate(radians(x))
#     line(0,0,100,0)
#     x=x+1
#     background(255)

# x=0
# z=random(0,150)
# def setup():
#     size(600,600)
    
# def draw():
#      global x
#      global z
#      background(0)
#      translate(300,300)
#      rotate(radians(x))
#      ellipse(0,x+0,z+x,z+x)
#      x=x+1

x=0

def setup():
     size(600,600)

def draw():
      global x
      translate(300,300)
      background(0)
      rotate(radians(x))
      ellipse(0,0,100,50)
      rect(50,-10,30,20)
      x=x+1
