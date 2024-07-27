import math
from itertools import permutations

# Define the cities' coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate distance matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = distance(cities[i], cities[j])

# Heuristic approach to find a route minimizing the maximum leg distance
def minimize_max_distance_tour():
    unvisited = set(range(1, n))
    tour = [0]
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current_city][x])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
        
    tour.append(0)  # return to the depot

    # Calculate the total distance and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        leg_distance = distances[tour[i]][tour[i+1]]
        total_cost += leg_distance
        if leg_distance > max_distance:
            max_distance = leg_distance

    return tour, total_cost, max_distance

# Perform the route calculation
tour, total_cost, max_distance = minimize_max_distance_tour()

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")