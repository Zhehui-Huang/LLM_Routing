import numpy as np
from scipy.spatial import distance
import random

# Cities coordinates
cities = {0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
          5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 
          10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
          15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)}

# Compute distance matrix
def compute_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i, j] = distance.euclidean(cities[i], cities[j])
    return dist_matrix

# Generate Initial Solution
def generate_initial_solution(cities, k=16):
    selected_cities = random.sample(list(cities.keys()), k)
    selected_cities.remove(0)
    selected_cities.insert(0, 0)  # Ensure depot is the first city
    return selected_cities

# Calculate total route cost
def calculate_route_cost(route, dist_matrix):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1))

# Perform shaking by swapping two cities
def shake(route):
    a, b = random.sample(range(1, 16), 2)  # Exclude depot at index 0 for swapping
    new_route = route[:]
    new_route[a], new_route[b] = new_route[b], new_route[a]
    return new_route

# Variable Neighborhood Descent
def vnd(route, dist_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, 16):
            for j in range(1, 16):
                if i != j:
                    new_route = route[:]
                    new_route[i], new_route[j] = new_route[j], new_space[i]
                    new_cost = calculate_route_cost(new_route, dist_matrix)
                    current_cost = calculate_route_cost(route, dist_matrix)
                    if new_cost < current_cost:
                        route = new_route
                        improved = True
    return route

# General Variable Neighborhood Search
def gvns(cities, nrst=100, k=16):
    dist_matrix = compute_distance_matrix(cities)
    # Initialize the best solution arbitrarily
    best_route = generate_initial_identity(cities, k)
    best_cost = calculate_route_cost(best_route, dist_matrix)
    
    for _ in range(nrst):
        current_route = generate_initial_solution(cities, k)
        current_route.append(current_route[0])  # Make the route circular

        while True:
            new_route = shake(current_route)
            new_route = vnd(new_route, dist_matrix)
            new_cost = calculate_route_cost(new_route, dist_matrix)

            if new_cost < best_cost:
                best_route = new_route
                best_cost = new_cost
                break
            else:
                # No improvement found, exiting the loop
                break

    return best_route, best_cost

# Solve the TSP with GVNS
best_tour, total_cost = gvns(cities)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")