import math
import itertools
import sys

# Cities and their coordinates
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of cities
n = len(coordinates)

# Calculate all pairs distances
distances = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Initialize the tour with the depot
tour = [0]
current_city = 0
visited = set(tour)

# Greedy approach to form an initial tour (not necessarily optimal at all)
while len(tour) < n:
    next_city = min((distances[current_city][j], j) for j in range(n) if j not in visited)[1]
    tour.append(next_city)
    visited.add(next_city)
    current_city = next_city

# Complete the tour by going back to the depot
tour.append(0)

# Calculate total travel cost and the maximum distance between consecutive cities
total_travel_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output the required results
output = {
    "Tour": tour,
    "Total travel cost": total_travel_cost,
    "Maximum distance between consecutive cities": max_distance
}

output