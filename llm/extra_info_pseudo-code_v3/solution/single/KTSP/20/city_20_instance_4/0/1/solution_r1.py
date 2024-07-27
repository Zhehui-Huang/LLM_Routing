import numpy as np
from scipy.spatial import distance
import random

# Cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Compute distance matrix
def compute_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = distance.euclidean(cities[i], cities[j])
    return dist_matrix

# Generate an initial solution
def generate_initial_solution(cities, k=16):
    city_indices = list(cities.keys())
    random.shuffle(city_indices)
    route = [0] + random.sample(city_indices[1:], k-1)
    if 0 not in route:
        route[0] = 0
    route.append(0)  # Make the route circular
    return route

# Calculate total route cost
def calculate_route_cost(route, dist_matrix):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route) - 1))

# Perform shaking by swapping two cities
def shake(route):
    k = len(route)
    a, b = random.sample(range(1, k-1), 2)  # Exclude depot at index 0 and last for swapping
    new_route = route[:]
    new_route[a], new_route[b] = new_route[b], new_route[a]
    return new_route

# Variable Neighborhood Descent
def vnd(route, dist_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 1):
            for j in range(i + 1, len(route) - 1):
                if i != j:
                    new_route = route[:]
                    new_route[i], new_route[j] = new_route[j], new_route[i]
                    new_cost = calculate_route_cost(new_route, dist_matrix)
                    current_cost = calculate_route_cost(route, dist_matrix)
                    if new_cost < current_cost:
                        route = new_route
                        improved = True
    return route

# General Variable Neighborhood Search
def gvns(cities, nrst=10, k=16):
    dist_matrix = compute_distance_matrix(cities)
    best_route = generate_initial_solution(cities, k)
    best_cost = calculate_route_cost(best_route, dist_matrix)

    for _ in range(nrst):
        current_route = generate_initial_solution(cities, k)
        while True:
            new_route = shake(current_route)
            new_route = vnd(new_route, dist_matrix)
            new_cost = calculate_route_cost(new_route, dist_matrix)

            if new_cost < best_cost:
                best_route, best_cost = new_route, new_cost
                break
            else:
                # Move to the next restart loop
                break

    best_route.pop()  # Remove the duplicated depot city at the end for correct outputs
    best_route.append(0)  # Make the route circular in output
    
    return best_route, best_cost

# Solve the TSP with GVDS
best_tour, total_cost = gvns(cities)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {float(total_cost)}")