import turtle
temp={'A':180,'W':90,'D':0,'S':-90}
def move_W():
    turtle.setheading(temp['W'])
    turtle.forward(50)
    turtle.stamp()

def move_A():
    turtle.setheading(temp['A'])
    turtle.forward(50)
    turtle.stamp()

def move_S():
    turtle.setheading(temp['S'])
    turtle.forward(50)
    turtle.stamp()

def move_D():
    turtle.setheading(temp['D'])
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()
    turtle.stamp()
    
turtle.shape('turtle')
turtle.stamp()
turtle.onkey(move_W,'w')
turtle.onkey(move_A,'a')
turtle.onkey(move_S,'s')
turtle.onkey(move_D,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
turtle.exitonclick()
