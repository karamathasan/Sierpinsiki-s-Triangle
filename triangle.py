import turtle as trtl

turtl = trtl.Turtle()
turtl.penup()
turtl.speed(0)


class Triangle:
  sideLength = 25
  startY = 200

  def drawTriangle(self):
    turtl.pendown()
    turtl.begin_fill()
    turtl.setheading(240)

    for i in range(2):
      turtl.forward(self.sideLength)
      turtl.left(120)
      self.vertices.append(self.getCoordinatePair())

    turtl.end_fill()
    turtl.penup()

  def goto(self, coordinatePair):
    turtl.goto(coordinatePair[0], coordinatePair[1])

  def shift(self, xshift, yshift):
    turtl.goto(turtl.xcor()+xshift, turtl.ycor()+yshift)

  def getCoordinatePair(self):
    x = turtl.xcor()
    y = turtl.ycor()
    return [x, y]

  def __init__(self, location=None, sidelength=None):
    self.location = [0, self.startY]

    if location != None:
      self.location = location
    if sidelength != None:
      self.sideLength = sidelength
    self.goto(self.location)

    self.vertices = []

  def __str__(self):
    return str(str(self.getCoordinatePair()) + str(self.vertices))
