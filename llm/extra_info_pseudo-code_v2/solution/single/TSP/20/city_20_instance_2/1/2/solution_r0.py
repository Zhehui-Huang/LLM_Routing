import math
from itertools import permutations

# City coordinates (depot + 19 cities)
coordinates = [
    (3, 26),    # Depot city 0
    (85, 72),   # City 1
    (67, 0),    # City 2
    (50, 99),   # City 3
    (61, 89),   # City 4
    (91, 56),   # City 5
    (2, 65),    # City 6
    (38, 68),   # City 7
    (3, 92),    # City 8
    (59, 8),    # City 9
    (30, 88),   # City 10
    (30, 53),   # City 11
    (11, 14),   # City 12
    (52, 49),   # City 13
    (18, 49),   # City 14
    (64, 41),   # City 15
    (28, 49),   # City 16
    (91, 94),   # City 17
    (51, 58),   # City 18
    (30, 48)    # City 19
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate pairwise distance matrix
N = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(N)] for i in range(N)]

# Initial tour using Nearest Neighbor heuristic from the depot
def nearest_neighbor_tour(start, num_cities):
    unvisited = set(range(1, num_cities))
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    tour.append(start)  # return to the depot
    return tour

def calculate_total_cost(tour):
    total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_cost

def lin_kernighan(tour):
    # Simplified Lin-Kernighan Heuristic Implementation
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+2, len(tour)-1):
                if distance_matrix[tour[i-1]][tour[i]] + distance_matrix[tour[j]][tour[j+1]] > distance_matrix[tour[i-1]][tour[j]] + distance_matrix[tour[i]][tour[j+1]]:
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
        if improved:
            best_tour = tour[:]
    return best_tour

# Initial tour and total cost
initial_tour = nearest_neighbor_tour(0, N)
improved_tour = lin_kernighan(initial_tour)
total_cost = calculate_total_cost(improved_tour)

# Output Results
print("Tour:", improved_tour)
print("Total travel cost:", total_cost)