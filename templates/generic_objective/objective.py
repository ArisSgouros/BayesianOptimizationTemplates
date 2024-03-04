
p1 = None
p2 = None

# Initialize contant parameters of the objective function
def Init():
   global p1
   global p2
   p1, p2 = 1.0, 1.0
   return

def Function(**xx):
   x = xx['x']
   y = xx['y']
   return -x ** 2 - (y - p1) ** 2 + p2
