import math
import itertools

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Coordinates of the cities including the depot city
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Simple greedy heuristic for TSP
def tsp_greedy(coordinates):
    n = len(coordinates)
    unvisited = set(range(1, n))
    tour = [0]  # starting from the depot city
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(coordinates[current_city], coordinates[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # return to the depot city
    return tour

# Calculate the cost of a given tour
def calculate_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

# Run the algorithm
tour = tsp_greedy(coordinates)
total_cost = calculate_tour_cost(tour, coordinates)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))