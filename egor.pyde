# x=0
# def setup():
#     size(600,600)
# def draw():
#     translate(300,300)
#     rotate(radians(x))
#     triangle(0,0,100,0,0,100)
#     triangle(0,0,-100,0,0,-100)
#     global x
# def keyPressed():
#     global x
#     if key == CODED:
#         if keyCode == UP:
#             x=x+1
#     if key == CODED:
#         if keyCode == DOWN:
#             x=x-1

# def setup():
#     size(600,600)
# def draw():    
#     if keyPressed:
#         background(255) 
#         rect(random(0,600),random(0,600),random(0,100),random(0,100))
#     fill(random(0,255),random(0,255),random(0,255))

# def setup():
#     size(600,600)
# def draw():    
#     if keyPressed:
#         fill(255,0,0)
#         textSize(random(0,100))
#         translate(300,300)
#         rotate(radians(random(0,600)))
#         text(u'e',random(0,600),random(0,600))

# x=0
# x2=0
# def setup():
#      size(600,600)
# def draw():
#      global x,x2
#      ellipse(300,x,100,100)
#      if x2 == 0:
#          x=x+1
#      if x2 == 1:
#          x=x-1
#      if x > 600:
#          x2=1
#      if x < 0:
#          x2=0
     
