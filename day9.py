#!/usr/bin/env python3
import numpy as np
import scipy.spatial as sp
import shapely

f = open("2025/ressources/day9.txt", "r") #Open File
lines = f.readlines() #Separate in lines

tiles = list()
for line in lines:
    line = line.replace("\n", "")
    parts = line.split(",")
    x, y = parts[0], parts[1]
    tile = (int(x), int(y))
    tiles.append(tile)
tiles.append(tiles[0])  # Close the polygon
tiles = np.array(tiles)

#Q1
convex_hull = sp.ConvexHull(tiles)
hull_points = tiles[convex_hull.vertices]
hull_diff = hull_points[:, None, :] - hull_points[None, :, :]
hull_area = np.abs(hull_diff[:, :, 0] + 1) * np.abs(hull_diff[:, :, 1] + 1)
maxArea = int(np.max(hull_area))

print("The area of the largest rectangle is: {}".format(maxArea))

#Q2
diff = tiles[:, None, :] - tiles[None, :, :]
areas = (np.abs(diff[:, :, 0])+1) * (np.abs(diff[:, :, 1])+1)
indexes = [(i, j) for i in range(len(tiles)) for j in range(len(tiles))]
areas = list(np.ravel(areas, order='C'))
areas, indexes = zip(*sorted(zip(areas, indexes), reverse=True))

polygon = shapely.geometry.Polygon(tiles)
for area, idx in zip(areas, indexes):
    i, j = idx
    p1 = tiles[i]
    p3 = tiles[j]
    p2 = (p3[0], p1[1])
    p4 = (p1[0], p3[1])
    rectangle = shapely.geometry.Polygon([p1, p2, p3, p4])
    if polygon.contains(rectangle):
        break

print("The area of the largest inscribed rectangle is: {}".format(area))