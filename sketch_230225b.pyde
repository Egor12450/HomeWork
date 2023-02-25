# x=0
# y=0
# x2=0
# y2=600
# def setup():
#     size(600,600)
# def draw():
#     global x
#     push()
#     rect(400,250,100,100)
#     fill(0)
#     rect(200,250,100,100)
#     pop()
# def mouseClicked():
#     global x,y,x2,y2
#     if mouseX > 400 and mouseX < 500 and mouseY > 250 and mouseY < 350:
#         while x < 600:
#             rect(x,y,10,10)
#             x=x+10
#         x=0
#         y=y+10
#     if mouseX > 200 and mouseX < 300 and mouseY > 250 and mouseY < 350:
#         while x2 < 600:
#             rect(x2,y2,10,10)
#             x2=x2+10
#         x2=0
#         y2=y2-10
