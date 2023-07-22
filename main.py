import triangle as t
import group as g

sidelength = 10
xshift = 0 
yshift = 0
recursionLimit = 7
recursionCounter = 1

def setshift(group):
  global xshift
  global yshift
  xshift = group.findLeftVertex()[0]
  yshift = t.Triangle.startY-group.findLeftVertex()[1]

def leftCopy(group):
  global sidelength
  global xshift
  global yshift
  subGroup = g.Group()
  for element in group.elements:
    if isinstance(element,t.Triangle):
      if group.elements.index(element) == 0:
        head = t.Triangle(None,sidelength)
        head.goto(group.location)
        head.shift(xshift,-yshift)
        head.drawTriangle()
        subGroup.append(head)
      elif group.elements.index(element) == 1:
        leftTriangle = t.Triangle(None,sidelength)
        leftTriangle.goto(head.vertices[0])
        leftTriangle.drawTriangle()
        subGroup.append(leftTriangle)
      elif group.elements.index(element) == 2:
        rightTriangle = t.Triangle(None,sidelength)
        rightTriangle.goto(head.vertices[1])
        rightTriangle.drawTriangle()
        subGroup.append(rightTriangle)
    else:
      if group.elements.index(element) == 0:
        element.location = group.location
      elif group.elements.index(element) == 1:
        element.location = group.elements[0].findLeftVertex()
      elif group.elements.index(element) == 2:
        element.location = group.elements[0].findRightVertex()
      subGroup.append(leftCopy(element))
  return subGroup

def rightCopy(group):
  global sidelength
  global xshift
  global yshift
  subGroup = g.Group()
  for element in group.elements:
    if isinstance(element,t.Triangle):
      if group.elements.index(element) == 0:
        head = t.Triangle(None,sidelength)
        head.goto(group.location)
        head.shift(-xshift,-yshift)
        head.drawTriangle()
        subGroup.append(head)
      elif group.elements.index(element) == 1:
        leftTriangle = t.Triangle(None,sidelength)
        leftTriangle.goto(head.vertices[0])
        leftTriangle.drawTriangle()
        subGroup.append(leftTriangle)
      elif group.elements.index(element) == 2:
        rightTriangle = t.Triangle(None,sidelength)
        rightTriangle.goto(head.vertices[1])
        rightTriangle.drawTriangle()
        subGroup.append(rightTriangle)
    else:
      if group.elements.index(element) == 0:
        element.location = group.location
      elif group.elements.index(element) == 1:
        element.location = group.elements[0].findLeftVertex()
      elif group.elements.index(element) == 2:
        element.location = group.elements[0].findRightVertex()
      subGroup.append(rightCopy(element))
  return subGroup

def expand(group):
  setshift(group)
  leftGroup = leftCopy(group)
  rightGroup = rightCopy(group)
  newGroup = g.Group()
  newGroup.append(group)
  newGroup.append(leftGroup)
  newGroup.append(rightGroup)
  return newGroup

def recur(group):
  global recursionLimit
  global recursionCounter
  recursionCounter += 1
  print("iteration " + str(recursionCounter))
  if recursionLimit == recursionCounter:
    return
  newGroup = expand(group)
  recur(newGroup)

base = t.Triangle(None, sidelength)
base.drawTriangle()
baseGroup = g.Group()
baseGroup.append(base)
#base case
for vertex in base.vertices:
  sub = t.Triangle(None, sidelength)

  baseGroup.append(sub)
  sub.goto(vertex)
  sub.location = vertex
  sub.drawTriangle()

recur(baseGroup)