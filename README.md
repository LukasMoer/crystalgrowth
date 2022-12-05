# Crystal Growth Simulation
December 2022

![Program Output](crystal.gif "Program outout")
Program output 

---

## Motivation
A close look at polycrystalline Materials under the microscope (especially with polarized light) often reveals impressing structures, where the individual crystals are visible and gives insights into the conditions under which the formation took place.

![Marble](Stained_marble.JPG "Crystal Structure of Pearlite and Ferrite in Steel. Source: Samson00, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons")

Crystal structure of quartz rich marble. 
Source:  Strekeisen, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons

Voronoi diagrams provide a very simple model to describe the growth and formation of the grain boundaries as seen in the pictures above. From each randomly scattered seed, a voronoi cell expands circular in all directions, and halts growth in a certain direction when it collides with a nother cell there. 


However, this model neglects some important behaviours: First, crystals are anisotropical and dont grow as circles. Second, the growth speed increases the larger a seed has already grown, as the Energy required to expand the crystal against its surface tension becomes less significant.

Hence, **this Program implements Voronoi Diagrams with polygonal growing seeds instead of circular growing ones** . The result is saved as a gif file.

## How it works
We start with an n x n grid (Parameter SIZE = n) and randomly select m pixels (Parameter SEEDS = m) on that grid. These are our crystal seeds! We create a list where we store them:
crystals = [ [x1,y1], [x2,y2],..]. 

By default, an empty pixel on the grid has the value -m, in order to enhance the contrast when plotting. An occupied pixel is assigned the index of the respective crystal.




## Todo
ffsdsdf

## References

