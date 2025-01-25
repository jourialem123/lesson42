import turtle
turtle.Screen().bgcolor("blue")

sc=turtle.Screen()
sc.title("star")
sc.setup(500,600)

tk=turtle.Turtle()

for i in range(3):
    tk.forward(100)
    tk.left(120)

tk.penup()
tk.forward(5)
tk.left(90)
tk.forward(60)
tk.right(90)
tk.pendown()

for i in range(3):
    tk.forward(100)
    tk.right(120)

    

turtle.done()    
