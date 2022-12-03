"""
CRYSTAL GROWTH SIMULATION
version 1
December 13, 2022
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

#PARAMETERS
SHAPE=4		#3=Triangle, 4=Square, 5=Pentagon,...
SIZE=126	#Lenght of the Grid in pixels
SEEDS=10	#Number of crystal seeds


#FUNCTIONS

def angle(y,x):
  """Returns the polar angle from cartesian coordinates """  
  if y>0:
    a=np.arctan2(y,x)
  else:
    a=np.arctan2(y,x)+2*math.pi
  return a


def polygon(R,a):
  """Returns the radial distance of a polygon in a certain angle a"""
  b=math.pi*(SHAPE-2)/(2*SHAPE)
  x=R*math.tan(b)/ (math.tan(a) + math.tan(b))
  y=R*math.tan(b)*math.tan(a)/ (math.tan(a) + math.tan(b))
  return ((x**2)+(y**2))**0.5
  
#MAIN
grid=np.zeros((SIZE,SIZE))	#Initialize the grid of pixels
grid=grid-SEEDS			#By default, empty pixels have a constant negative value
				            #while occupied pixels have a value from 0,1,2...to the number of crystals
crystals=[]			
for i in range(SEEDS):		#Make a List that contains the random positions& orientations of the crystals
  x=random.randint(1,SIZE-2)
  y=random.randint(1,SIZE-2)
  a=math.pi*random.random()
  grid[y][x]=i
  crystals.append([x,y,a])

fig = plt.figure()		#Object for animation
frames=[]			#List, where the frames for the animation will be saved

R=1				    #We let the crystals grow until we reach a stationary state
change=1			#and the crystals reached a certain threshold size
previous_sum=np.sum(grid)

threshold = int((SIZE*SIZE/SEEDS)**(1/2))
while change!=0 or R<threshold:	
  for i in range(SIZE):		      #In every growth step, go through every pixel.
    for j in range(SIZE):	      #column by column (j), row by row (i)
      if grid[i][j]==-SEEDS:	  #If the pixel is not occupied yet..
        for n in range(SEEDS):	#check the distances to each crystal seed..
          dx=j-crystals[n][0]	
          dy=i-crystals[n][1]	          
          distance=((dx**2)+(dy**2))**0.5
          
          alpha=angle(dy,dx)-crystals[n][2]
          alpha=alpha%(2*math.pi/SHAPE)
          
          Rcrystal=polygon(R,alpha)	#compute size of that crystal in polar coords 
          
          if distance<=Rcrystal:	#and if the pixel is already inside the crystals range
            grid[i][j]=n	        #then mark it accordingly, occupied by crystal nr. n
            break
  change=np.sum(grid)-previous_sum
  previous_sum=np.sum(grid)
  frames.append([plt.imshow(grid, cmap='bone', animated=True,vmin=-10)])
  R+=1

for _ in range(len(frames)):	#Duplicate the last frame to make the gif pause in its final state
  frames.append([plt.imshow(grid, cmap='bone', animated=True,vmin=-10)])

ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True, repeat_delay=1000)
ani.save('crystal.gif', dpi=80, writer='imagemagick')
