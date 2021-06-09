#determine pi, based on a random number between 0 and 1

import random 

def pi(n):
  pts_circle = 0
  pts_total = 0
  for _ in range(n):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    distance = x**2 + y**2
    if distance <= 1:
      pts_circle += 1
    pts_total += 1
    
 return 4 +  pts_circle/pts_total   
    
    
    
class Random:
  def __init__(self, pts_circle, pts_total, distance):
    self.pts_circle = pts_circle
    self.pts_total = pts_total 
    self.distance = distance
    
 def estimate_pi(n, x, y):
  self.x = x
  self.y = y
  self.pts_circle = 0
  self.pts_total = 0
  for _ in range(n):
    self.x = random.uniform(0,1)
    self.y = random.uniform(0,1)
    self.distance = self.x**2 + self.y**2
    if self.distanc <= 1:
      self.pts_circle += 1
    pts_total += 1

return 4 + pts_circle/pts_total
