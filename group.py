import triangle as t


class Group:
  # sideLength = 50

  def append(self, group):
    self.elements.append(group)

  def add(self, group, index):
    if index > 2:
      raise Exception("invalid index")
    self.elements[index] = group

  def set(self, elements):
    for element in elements:
      self.add(element, elements.index(element))

  def getLocation(self):
    if isinstance(self.elements[0], t.Triangle):
      self.location = self.elements[0].location
      return self.elements[0].location
    return self.elements[0].getLocation

  def findLeftVertex(self):
    if isinstance(self.elements[1], t.Triangle):
      return self.elements[1].vertices[0]
    return self.elements[1].findLeftVertex()

  def findRightVertex(self):
    if isinstance(self.elements[2], t.Triangle):
      return self.elements[2].vertices[1]
    return self.elements[2].findRightVertex()

  def findVertices(self):
    left = self.findLeftVertex()
    self.vertices[0] = left
    right = self.findRightVertex()
    self.vertices[1] = right
    return [left, right]

  def __init__(self):
    self.location = [0,t.Triangle.startY]
    self.elements = []
    self.vertices = [None,None]

  def __str__(self):
    return str(self.elements)
    # return str([self for self in globals() if globals()[self] is self])
