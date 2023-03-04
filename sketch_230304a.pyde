# x=0
# y=300
# z=300
# def setup():
#     size(600,600)
# def draw():
#         global x,y,z
#         while x < 600:
#             line(x,300,x,y)
#             x=x+10
#             y=y-5
#         z=z+5

# size(600,600)
# for y in range(12):
#     for x in range(12):
#         fill(random(0,255),random(0,255),random(0,255))
#         rect(x*50,y*50,50,50)
        
x=0
size(600,600)
global x
for y in range(12):
    for x in range(12):
        if x == 0:
            x = 1
        else:
            x = 0
        if x == 0:
            fill(0)
        if x == 1:
            fill(255)
        rect(x*50,y*50,50,50)
