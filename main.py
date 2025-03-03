import turtle as turtle_module
import random
from turtle import Screen

turtle_module.colormode(255)
tim = turtle_module.Turtle()
all_colors = [(229, 222, 210), (223, 159, 80), (39, 107, 149), (118, 164, 192), (150, 63, 88), (207, 134, 157), (180, 160, 35), (28, 133, 96), (213, 86, 59), (120, 181, 152), (164, 80, 52), (200, 84, 111), (208, 225, 215), (143, 31, 40), (54, 167, 135), (232, 198, 110), (201, 219, 227), (229, 206, 214), (6, 109, 90), (41, 160, 185), (117, 114, 163), (238, 159, 174), (30, 62, 112), (153, 211, 199), (235, 169, 158), (26, 64, 57), (125, 38, 35), (28, 58, 84), (150, 208, 217), (69, 39, 50), (65, 44, 41), (6, 96, 116), (185, 186, 207), (81, 83, 26)]
tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    tim.color(random.choice(all_colors))
    tim.dot(20)
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen =Screen()
screen.exitonclick()