import turtle as trtl
painter = trtl.Turtle()

painter.penup()
painter.goto(-100,0)
painter.pendown()

painter.right(90)
painter.circle(100)

painter.penup()
painter.goto(-30,0)
painter.pendown()

painter.circle(30)

painter.pencolor("orange")
painter.penup()
painter.goto(-65,0)
painter.pendown()

painter.pensize(67.5)
painter.circle(65)

wn = trtl.Screen()
wn.mainloop()