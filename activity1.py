import turtle

turtle.Screen().bgcolor("lightgreen")

sc=turtle.Screen()
sc.title("Square")
sc.setup(300,400)

tk=turtle.Turtle()

for i in range(4):
    tk.forward(100)
    tk.left(90)

turtle.done()
