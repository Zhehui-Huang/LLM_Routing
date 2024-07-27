import numpy as np
from itertools import permutations
from scipy.spatial.distance import euclidean

# Defining the coordinates of each city
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Compute distance matrix
n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i, j] = euclidean(cities[i], cities[j])

def calculate_total_distance(tour):
    total_dist = 0
    for i in range(len(tour)-1):
        total_dist += distance_matrix[tour[i], tour[i+1]]
    return total_dist

# Greedy algorithm to get a starting solution: Nearest Neighbor
def greedy_starting_sol():
    unvisited = set(range(1, n_cities))
    tour = [0]  # starts at the depot
    current = 0

    while len(tour) < 10:
        next_city = min(unvisited, key=lambda x: distance_matrix[current, x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(0)  # return to the depot
    return tour

# k-TSP with GVNS: Variable Neighborhood Search
def variable_neighborhood_search(initial_tour):
    current_tour = initial_tour[:]
    best_tour = initial_tour[:]
    best_cost = calculate_total_distance(initial_tour)
    
    # Define the neighborhood by simple permutations
    for i in range(1, len(initial_tour)-2):
        for j in range(i+1, len(initial_tour)-1):
            new_tour = current_tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
            if new_tour[-1] != 0:
                continue
            
            new_cost = calculate_total_distance(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour[:]
                best_cost = new_cost
    
    return best_tour, best_cost

# Initialize the tour
initial_tour = greedy_starting_sol()
optimized_tour, total_cost = variable_neighborhood_search(initial_tour)

# Output the result
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)