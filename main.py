import colorgram
import turtle  as t
import random

screen=t.Screen()
screen.bgcolor("#ffb3b3")
# Extract 6 colors from an image.
colors = colorgram.extract('wallpapersden.com_goku-ultra-instinct-hd-digital-art_2563x1191.jpg', 800)
t.colormode(255)
#print(colors)
rgb_color=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new=(r,g,b)
    rgb_color.append(new)
    tim=t.Turtle()

tim.speed("fastest")
tim.hideturtle()
tim.goto(-400, -300)
for j in range(10):

    for i in range(17):
        tim.dot(20,random.choice(rgb_color))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(850)
    tim.setheading(0)

screen.exitonclick()
