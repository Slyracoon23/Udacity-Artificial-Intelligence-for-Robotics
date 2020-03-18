#!/usr/bin/env python3
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import from_levels_and_colors

#Number of grid cells
n_cells = 100

p_hit = 0.6
p_miss = 0.2
p_exact = 0.8
p_undershoot = 0.1
p_overshoot = 0.1

#Start with uniform probability distribution i.e. the robot could be anywhere
# p = [1/n_cells for _ in range(n_cells)]
p = n_cells * [1/n_cells]



#Or we know where we start
#p = [0 for _ in range(n_cells)]
#p[0] = 1
#p = n_cells * [0]
#p[0] = 1

# create doors
world = [1 if random.random() > 0.8 else 0 for _ in range(n_cells)]
#world = [0, 1, 1, 0, 0]
colors = ["white", "black"]
levels = [0, 1, 2]
cmap, norm = from_levels_and_colors(levels, colors)

def sense(p, Z):
    q = []
    for i in range(n_cells):
        hit = (world[i] == Z)
        q.append(p[i]*(hit*p_hit + (1 - hit)*p_miss))
    norm = sum(q)
    q = [q[i]/norm for i in range(n_cells)]
    return q

def move(p, U):
    q = []
    for i in range(n_cells):
        s = p_exact*p[(i-U)%len(p)]
        s += p_overshoot*p[(i-U-1)%len(p)]
        s += p_undershoot*p[(i-U+1)%len(p)]
        q.append(s)
    return q




