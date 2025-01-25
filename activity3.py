import turtle

sc=turtle.Screen()
t=turtle.Turtle()
sc.bgcolor("black")
color=["red","orange","yellow","green","blue","purple"]
t.hideturtle()
t.speed("fastest")

while True:
    for x in range(200):
        t.pencolor(color[x%len(color)])
        t.width(x/100+1)
        t.forward(x)
        t.left(59)
    
    t.right(239) 
    for x in range(200,0,-1):
        t.pencolor("black") 
        t.width(x/100+7)
        t.forward(x)
        t.right(59)

turtle.done()        



