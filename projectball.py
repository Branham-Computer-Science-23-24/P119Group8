import turtle as trtl
painter = trtl.Turtle()

painter.pensize(50)
painter.circle(85)
painter.pencolor("red")
painter.pensize(45)
painter.circle(85)

painter.goto(0,50)
painter.pensize(75)
painter.circle(35)

painter.goto(-40,130)
painter.pencolor("white")
painter.pensize(15)
painter.circle(5)

wn = trtl.Screen()
wn.mainloop()
