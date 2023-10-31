import turtle as trtl
painter = trtl.Turtle()

dogbird = 'birddog.gif'

wn = trtl.Screen()
wn.addshape(dogbird)

painter.penup()
painter.goto(-400,0)
painter.pendown()

painter.pencolor("yellow")
painter.pensize(800)
painter.forward(800)

painter = trtl.Turtle(shape = dogbird)

painter.shape(dogbird)

############################# Dog Code

painter.penup()
painter.pencolor("black")
painter.goto(0,0)
painter.pendown()

painter.pensize(5)
painter.circle(40)

painter.penup()
painter.goto(22,75)
painter.pendown()

painter.pensize(10)
painter.goto(40,30)
painter.goto(50,75)
painter.goto(22,75)

painter.penup()
painter.goto(-22,75)
painter.pendown()

painter.goto(-40,30)
painter.goto(-50,75)
painter.goto(-22,75)

painter.penup()
painter.goto(0,30)
painter.pendown()

painter.pensize(6)
painter.circle(1)

painter.penup()
painter.goto(15,50)
painter.pendown()

painter.pensize(3)
painter.circle(1)

painter.penup()
painter.goto(-15,50)
painter.pendown()

painter.circle(1)

painter.penup()
painter.goto(-5,20)
painter.pendown()

painter.goto(5,20)

painter.penup()
painter.goto(20,5)
painter.pendown()

painter.pensize(5)
painter.goto(50,-75)

painter.penup()
painter.goto(-20,5)
painter.pendown()

painter.goto(-50,-75)
painter.goto(50,-75)

painter.penup()
painter.goto(25,-10)
painter.pendown()

painter.goto(15,-40)
painter.goto(0,-10)

painter.penup()
painter.goto(-25,-10)
painter.pendown()

painter.goto(-15,-40)
painter.goto(0,-10)

painter.penup()
painter.goto(50,-75)
painter.pendown()

painter.pensize(7)
painter.goto(55,-65)
painter.goto(60,-70)
painter.goto(65,-55)
painter.goto(70,-60)
painter.goto(75,-45)
painter.goto(80,-50)
painter.goto(85,-35)
painter.goto(90,-40)

############################# Ball Code

painter.penup()
painter.goto(200,100)
painter.pendown()

painter.goto(200,100)
painter.pensize(50)
painter.circle(85)
painter.pencolor("red")
painter.pensize(35)
painter.circle(85)

painter.goto(200,150)
painter.pensize(75)
painter.circle(35)

painter.goto(170,200)
painter.pencolor("white")
painter.pensize(15)
painter.circle(5)

############################# Bagel Code

painter.penup()
painter.goto(-100,200)
painter.pendown()

painter.pencolor("black")
painter.right(90)
painter.circle(100)

painter.penup()
painter.goto(-30,200)
painter.pendown()

painter.circle(30)

painter.pencolor("orange")
painter.penup()
painter.goto(-65,200)
painter.pendown()

painter.pensize(67.5)
painter.circle(65)

############################# Bacon Code

bacon_color = 0

painter.penup()
painter.pencolor("red")
painter.right(90)
painter.pensize(50)
painter.goto(-90,125)
painter.pendown()

while (bacon_color <= 3):
 painter.pencolor("red")
 painter.forward(200)
 painter.penup()
 painter.backward(200)
 painter.right(90)
 painter.forward(50)
 painter.left(90)
 painter.pendown()
 bacon_color = bacon_color + 1
 while (bacon_color == 1):
  painter.pencolor("pink")
  painter.forward(200)
  painter.penup()
  painter.backward(200)
  painter.right(90)
  painter.forward(50)
  painter.left(90)
  painter.pendown()
  bacon_color = bacon_color + 2

wn = trtl.Screen()
wn.mainloop()