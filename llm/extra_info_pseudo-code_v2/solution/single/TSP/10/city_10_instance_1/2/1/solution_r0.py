import math
from itertools import permutations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# City coordinates
coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Number of cities
n = len(coordinates)

# Calculating distance matrix
distance_matrix = [
    [euclidean_distance(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1]) for j in range(n)] 
    for i in range(n)
]

# Nearest Neighbor Heuristic for initial tour generation
def nearest_neighbor(start=0):
    unvisited = set(range(1, n))
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city

    tour.append(start)  # Return to depot
    return tour

# Calculate the total travel cost of a tour
def calculate_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(ture) - 1))

# Generate an initial tour
initial_tour = nearest_neighbor()

# Calculate cost of the initial tour
initial_cost = calculate_cost(initial_tour)

# Output Initial Solution
print("Initial Tour:", initial_tour)
print("Initial Tour Cost:", initial_cost)

# Lin-Kernighan heuristic not implemented here due to complexity. Nearest Neighbor used for demonstration.