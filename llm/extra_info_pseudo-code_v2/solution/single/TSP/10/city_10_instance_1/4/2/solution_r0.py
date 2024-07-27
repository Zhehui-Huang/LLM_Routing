import numpy as np
from scipy.spatial.distance import euclidean

# Cities and their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Initialize the robot's path starting from the depot city
path = [0]

# Calculate distance between two cities
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Compute the initial path using the nearest neighbor heuristic
unvisited = set(cities.keys()) - {0}

current_city = 0
while unvisited:
    next_city = min(unvisited, key=lambda city: distance(current_city, city))
    path.append(next_city)
    unvisited.remove(next_city)
    current_city = next_city

# Adding the depot city to complete the tour
path.append(0)

# Calculate the total cost (travel distance)
total_distance = sum(distance(path[i], path[i+1]) for i in range(len(path)-1))

# Output the optimal path and cost
print("Tour:", path)
print("Total travel (cost):", total_distance)