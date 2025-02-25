#! /usr/bin/env python
"""
Solar.py is a program that provides a simple 3D visualization 
of the solar system of the first six planets.

It uses the facilities provided by the visual package, 
create an animation of the solar system that shows the Sun and the 
motions of Mercury, Venus, Earth, Mars, Jupiter, and Saturn.

 Paul Eugenio 
 PHZ4151C
 Jan 27, 2019
"""

import vpython as vp
import numpy as np

framerate = 30
tscale = 250
sizescale = 2
radscale = 1000
nplanets = 6

sunsize = 30000.0
# plantary data
orbit = [ 88.0,224.7,365.3,687.0,4331.6,10759.2,30799.1,60190.0 ]
size = [ 2240, 6052, 6371, 3386, 69173, 57316, 25266, 24553 ]
rad = [ 57.9, 108.2, 149.6, 227.9, 778.5, 1433.4, 2876.7, 4503.4 ]
colors = [vp.color.magenta, vp.color.green, vp.color.blue, vp.color.red, vp.color.orange, vp.color.cyan]

graph1=vp.canvas(width=800, height=800)
# create the sun
vp.sphere(pos=vp.vector(0,0,0), radius=sunsize, color=vp.color.yellow)

# create the planets
planet = np.empty(nplanets, vp.sphere)
for p in range(nplanets):
    x = radscale*rad[p]
    y = 0.0
    planet[p] = vp.sphere(pos=vp.vector(x,y,0), radius=sizescale*size[p], color=colors[p], make_trail=False)

# begin time
t = 0.0
counter=0
while True:
    vp.rate(framerate) 
    t += tscale/framerate

# move planets in their orbits
    for p in range(nplanets):
        x = radscale*rad[p]*np.cos(2*np.pi*t/orbit[p])
        y = radscale*rad[p]*np.sin(2*np.pi*t/orbit[p])
        planet[p].pos = vp.vector(x, y, 0)

    counter+=1
#    graph1.capture('test_'+str(counter))
