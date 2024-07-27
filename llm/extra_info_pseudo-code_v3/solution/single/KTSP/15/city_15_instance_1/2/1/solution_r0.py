import random
import math

# Define city locations
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialize a distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Generate an initial random solution
def generate_initial_solution():
    route = [0] + random.sample(range(1, len(cities)), 5)
    route.append(0)
    return route

# Calculate the total tour cost
def calculate_cost(route):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Neighborhood structures
def shake(route):
    new_route = route[1:-1]
    random.shuffle(new_route)
    return [0] + new_route + [0]

def vnd(route):
    best_route = route[:]
    best_cost = calculate_cost(route)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                if i != j:
                    new_route = route[:]
                    new_route[i], new_route[j] = new_route[j], new_route[i]
                    new_cost = calculate_cost(new_route)
                    if new_cost < best_cost:
                        best_route, best_cost = new_route[:], new_cost
                        improved = True
    return best_route

# Main GVNS function
def gvns_k_tsp(nrst):
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    
    for _ in range(nrst):
        current_solution = generate_initial_solution()
        current_cost = calculate_cost(current_solution)
        
        while True:
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution)
            new_cost = calculate_cost(new_solution)
            
            if new_cost < current_cost:
                current_solution, current_cost = new_solution, new_cost
            else:
                break
        
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
            
    return best_solution, best_cost

# Execute and print the results
n_restarts = 100
final_route, final_cost = gvns_k_tsp(n_restarts)
print(f"Tour: {final_route}")
print(f"Total travel cost: {final_cost:.2f}")