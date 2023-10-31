import turtle as trtl
painter = trtl.Turtle()

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

wn = trtl.Screen()
wn.mainloop()