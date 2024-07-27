import math
import random

# City coordinates (city 0 is depot)
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Distance matrix initialisation
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')  # Infinity distance to itself for avoidance in TSP

# Generate initial tour - naive greedy approach
def get_initial_tour():
    unvisited = list(range(1, n)) # excluding depot city
    tour = [0]  # start at the depot
    current = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # return to the depot
    return tour

# Calculate total travel cost for the current tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i + 1]]
    return total_cost

# Simple 2-opt swap to improve the tour
def two_opt(tour):
    min_change = None
    best_tour = tour[:]
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            if j - i == 1: continue  # skip adjacent edges
            new_tour = tour[:]
            new_tour[i:j] = tour[i:j][::-1] # reverse segment
            change = calculate_total_cost(new_tour) - calculate_total_cost(tour)
            if min_change is None or change < min_change:
                min_change = change
                best_tour = new_tour
    return best_tour

# Main procedure
def solve_tsp():
    tour = get_initial_tour()
    improved = True
    while improved:
        new_tour = two_opt(tour)
        if calculate_total_cost(new_tour) < calculate_total_cost(tour):
            tour = new_tour
        else:
            improved = False

    tour_cost = calculate_total_cost(tour)
    return tour, tour_cost

# Solve the TSP
final_tour, final_cost = solve_tsp()
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")