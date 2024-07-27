import numpy as np
from itertools import permutations
from math import sqrt, inf

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate distance matrix
def generate_distance_matrix(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean-distance(cities[i], cities[j])
    return distances

distance_matrix = generate_distance_matrix(cities)

# Initial subset selection function
def initial_subset_selection(cities, k):
    # Starting at depot, add closest cities first until k cities are selected
    selected_cities = [0]
    sorted_cities = sorted(cities.items(), key=lambda x: euclidean_distance(cities[0], x[1]))
    for i, _ in sorted_cities:
        if i != 0:
            selected_cities.append(i)
            if len(selected_cities) == k:
                break
    return selected_cities

# Calculate the tour cost
def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance_matrix[tour[i - 1]][tour[i]]
    # return to the depot
    total_cost += distance_matrix[tour[-1]][tour[0]]
    return total_cost

# General VNS metaheuristic
def general_vns(cities, k, distance_matrix):
    best_tour = initial_subset_selection(cities, k)
    best_cost = calculate_tour_cost(best_tour, distance_matrix)
    no_improvement = 0
    
    while no_improvement < 100:
        current_tour = best_tour[:]
        # Shuffle current tour as part of local search
        np.random.shuffle(current_tour[1:])
        current_cost = calculate_tour_cost(current_tour, distance_matrix)
        
        if current_cost < best_cost:
            best_tour = current_tour[:]
            best_cost = current_cost
            no_improvement = 0
        else:
            no_improvement += 1
    
    return best_tour, best_cost

# Run the optimization strategy
k = 8
best_tour, best_cost = general_vns(cities, k, distance_matrix)

# Format for output
tour_output = best_tour + [best_tour[0]]
print("Tour:", tour_output)
print("Total travel cost:", best_cost)