import numpy as as np
from math import sqrt

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(a, b):
    """ Calculate the Euclidean distance between two points """
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Distance matrix
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i, j] = euclidean_distance(cities[i], cities[j])

# A simple TSP solving crude approach: Nearest Neighbour for initial path
def nearest_neighbour_tour(start=0):
    tour = [start]
    used = set(tour)
    total_cost = 0
    
    current = start
    while len(tour) < n:
        next_city = min(((distances[current, j], j) for j in range(n) if j not in used), default=(None, None))
        if next_city[1] is None:
            break
        total_cost += next_city[0]
        current = next_city[1]
        tour.append(current)
        used.add(current)
    
    # Return to the depot
    tour.append(start)
    total_cost += distances[current][start]
    
    return tour, total_cost

# Generate an initial tour and calculate its total cost
tour, total_cost = nearest_neighbour_tour()

# Output the desired tour and total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)