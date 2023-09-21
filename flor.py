Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
... 
... screen = turtle.Screen()
... screen.bgcolor("white")
... 
... flower = turtle.Turtle()
... flower.shape("turtle")
... flower.color("red")
... flower.speed(10)  
... 
... flower.penup()
... flower.goto(0, -200)
... flower.pendown()
... flower.goto(0, 0)
... 
... for _ in range(36):   
...     flower.color("red")
...     flower.forward(100)
...     flower.right(45)
...     flower.color("yellow")
...     flower.forward(50)
...     flower.right(135)
...     flower.color("red")
...     flower.forward(100)
...     flower.right(45)
...     flower.color("yellow")
...     flower.forward(50)
...     flower.right(135)
...     flower.right(10)  
... 
