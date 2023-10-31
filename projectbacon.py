import turtle as trtl
bacon = trtl.Turtle()
bacon_color = 0

bacon.backward(100)
bacon.pencolor("red")
bacon.pensize(50)

while (bacon_color <= 3):
 bacon.pencolor("red")
 bacon.forward(200)
 bacon.penup()
 bacon.backward(200)
 bacon.right(90)
 bacon.forward(50)
 bacon.left(90)
 bacon.pendown()
 bacon_color = bacon_color + 1
 while (bacon_color == 1):
  bacon.pencolor("pink")
  bacon.forward(200)
  bacon.penup()
  bacon.backward(200)
  bacon.right(90)
  bacon.forward(50)
  bacon.left(90)
  bacon.pendown()
  bacon_color = bacon_color + 2


wn = trtl.Screen()
wn.mainloop()