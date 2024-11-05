import turtle


screen = turtle.Screen()
screen.bgcolor("white")  


spiral = turtle.Turtle()
spiral.shape("turtle")  
spiral.color("green")   
spiral.speed(10)        


def draw_spiral():
    size = 1  
    for i in range(100):  
        spiral.forward(size)
        spiral.left(30)  
        size += 2        


draw_spiral()


spiral.hideturtle()


screen.exitonclick()
