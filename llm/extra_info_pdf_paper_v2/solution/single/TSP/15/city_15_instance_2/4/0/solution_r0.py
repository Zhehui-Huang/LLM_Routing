import math
from itertools import permutations

# Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculating the total tour cost
def tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return total_cost

# Coordinates of cities including depot
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Find a potential optimal tour using a greedy algorithm as a simple heuristic (Nearest Neighbor)
def nearest_neighbor_tour(start, coordinates):
    n = len(coordinates)
    unvisited = set(range(1, n))
    tour = [start]
    current_city = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(coordinates[current_city], coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start) # return to the depot
    return tour

# Get initial tour
initial_tour = nearest_neighbor_tour(0, coordinates)

# Calculate initial tour cost
initial_cost = tour_cost(initial_tour, coordinates)

# Output the results
print("Tour: ", initial_tour)
print("Total travel cost: {:.2f}".format(initial_cost))