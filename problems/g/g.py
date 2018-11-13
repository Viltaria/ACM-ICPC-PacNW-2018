import math

def distance(x1, y1, x2, y2): # Find distance between two given points
  return math.sqrt(
    ((y2 - y1) ** 2)
    +
    ((x2 - x1) ** 2)
    )

goat_x, goat_y, x1, y1, x2, y2 = raw_input().split(' ')

goat_x = int(goat_x)
goat_y = int(goat_y)
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

def collision(goat_x, goat_y, x1, y1, x2, y2):
  # Check if the closest point of is on one of the sides
  if goat_x < x1 and goat_y > y1 and goat_y < y2:
    return distance(x1, goat_y, goat_x, goat_y)
  elif goat_x > x1 and goat_x < x2 and goat_y < y1:
    return distance(goat_x, y1, goat_x, goat_y)
  elif goat_x > x2 and goat_y > y1 and goat_y < y2:
    return distance(x2, goat_y, goat_x, goat_y)
  elif goat_x > x1 and goat_x < x2 and goat_y > y2:
    return distance(goat_x, y2, goat_x, goat_y)
  # Check if the closest point is on one of the corners
  elif goat_x <= x1 and goat_y >= y2:
    return distance(x1, y2, goat_x, goat_y)
  elif goat_x <= x1 and goat_y <= y1:
    return distance(x1, y1, goat_x, goat_y)
  elif goat_x >= x2 and goat_y <= y1:
    return distance(x2, y1, goat_x, goat_y)
  elif goat_x >= x2 and goat_y >= y2:
    return distance(x2, y2, goat_x, goat_y)

print "%.3f" % collision(goat_x, goat_y, x1, y1, x2, y2)
