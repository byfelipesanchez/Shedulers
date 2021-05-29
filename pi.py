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
    
    
    
