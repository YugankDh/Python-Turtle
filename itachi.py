import turtle 
t = turtle.Turtle()
t.speed(10)
t.penup()
t.color("black","red")
t.pensize(4)
t.goto(0,200)
t.pendown()
t.begin_fill()
t.circle(-200)
t.end_fill()
t.right(5)
t.forward(10)
t.right(145)
t.color("black","black")
t.begin_fill()
for i in range(40):
  t.forward(7)
  t.left(2)
t.right(95)
for i in range(24):
  t.forward(5)
  t.right(2)
t.left(127)
for i in range(20):
  t.forward(2)
  t.left(1)
t.left(25)
for i in range(45):
  t.forward(7)
  t.left(2)
t.right(95)
for i in range(21):
  t.forward(5)
  t.right(2)
t.left(127)
for i in range(20):
  t.forward(2)
  t.left(1)
t.left(25)
for i in range(45):
  t.forward(7)
  t.left(2)
t.right(95)
for i in range(20):
  t.forward(5)
  t.right(2)
t.left(127)
for i in range(20):
  t.forward(2)
  t.left(1)
t.end_fill()
t.penup()
t.goto(0,40)
t.color("black","red")
t.begin_fill()
t.circle(30)
t.end_fill()
t.hideturtle()
turtle.done()

  
  
  
  
  
  
  
  
