
class Direction():

  NORTH = 'w'
  SOUTH = 's'
  WEST = 'a'
  EAST = 'd'

class MainSymbol():

  score = 0

  def __init__(self, symbol, startX = 20, startY = 10, velx = 2, vely = 1, trace = '.'):

    self.symbol = symbol

    self.x = startX
    self.y = startY

    self.velx = velx
    self.vely = vely

    self.trace =  trace


  def move(self, direction):

    if direction == Direction.SOUTH:
      self.y += self.vely
    elif direction == Direction.NORTH:
      self.y -= self.vely

    elif direction == Direction.WEST:
      self.x -= self.velx
    elif direction == Direction.EAST:
      self.x += self.velx



