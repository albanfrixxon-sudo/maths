#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# ________________ ignore this section of comments, misread the graph __________

# Either doesn't work for negative scale factors (most probable) or doesn't work for centre of enlargement except origin (less likely but haven't tested either yet).

# Works for other use
# this graph isn't the best

# ____________________________________________________________________________

# turns out the program does work but the graph is extremely odd
# is usable (i think)


choice = None
points = []
newPoints = []

print("\nInput coordinates as 'x y'.\n")

print("(C)entre of origin - (S)cale factor - (N)umber of points - (Q)uit")

while not choice == "q":
    
    choice = input().lower()
    
    if choice == "c":
        cofe = np.array(input("Centre ┃ ").split(), dtype=int)
    
    elif choice == "s":
        sf = int(input("Scale ┃ "))
        
    elif choice == "n":
        n = int(input("Number ┃ "))

print("\n")

print("          x y")
for num in range(1, n + 1):
    points.append(np.array(input(f"Point {num} ┃ ").split(), dtype=int))
    
for num in range(n):
    newPoints.append(((points[num] - cofe) * sf) + cofe)

x, y = zip(*points)
x = list(x) + [x[0]]
y = list(y) + [y[0]]

xNew, yNew = zip(*newPoints)
xNew = list(xNew) + [xNew[0]]
yNew = list(yNew) + [yNew[0]]

plt.plot(x, y, color='blue', linewidth=1)
plt.plot(xNew, yNew, color='red', linewidth=1)
plt.gca().set_aspect('equal')

print("\nYour updated point coordinates are, as displayed:\n")
print("          x y")
for current in range(n):
    print(f"Point {current + 1} ┃ {xNew[current]} {yNew[current]}")
print()

plt.show()

