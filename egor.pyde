# x=[100,400,200,300]
# y=[0,0,255,255,0,0]
# size(600,600)
# fill(y[0],y[1],y[2])
# ellipse(300,100,x[0],x[1])
# fill(y[3],y[4],y[5])
# ellipse(300,300,x[2],x[3])

# x = [0,24,36,49,75,81,100,143,200,220,243,298,331,360,401,461,489,523,570]
# y = [0,40,10, 43,32,80,54,0,40,10, 43,11,23,21,54,45,67,0,40,10, 43,11,23]

# def setup():
#     size(600,400)
#     stroke(255)
#     strokeWeight(4)
#     background(0)
    
# def draw():
#     background(0)
#     for index in range(len(x)):    
#         point(x[index],y[index])
#         y[index] = y[index] + random(1,100)
#         if y[index]>400:
#             y[index] = y[index] - 400

# x = [0,24,36,49,75,81,100,143,200,220,243,298,331,360,401,461,489,523,570]
# y = [0,40,10, 43,32,80,54,0,40,10, 43,11,23,21,54,45,67,0,40,10, 43,11,23]
# z = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,30]

# def setup():
#     size(600,400)
#     stroke(255)
#     strokeWeight(4)
#     background(0)
    
# def draw():
#     background(0)
#     for index in range(len(x)):    
#         point(x[index],y[index])
#         y[index] = y[index] + z[index]
#         if y[index]>400:
#             y[index] = y[index] - 400
