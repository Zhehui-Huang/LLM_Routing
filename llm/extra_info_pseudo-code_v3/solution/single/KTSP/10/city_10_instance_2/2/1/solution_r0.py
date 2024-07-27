import numpy as np
import random

# Define city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

num_cities = len(cities)
distance_matrix = np.zeros((num_cities,num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Define functions for GVNS
def create_initial_solution():
    solution = [0] + random.sample(list(cities.keys())[1:], 5)
    solution.append(0)  # Append depot at the end to ensure round trip
    return solution

def calculate_tour_cost(solution):
    return sum(distance_matrix[solution[i], solution[i+1]] for i in range(len(solution)-1))

def shake(solution):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [0] + new_solution + [0]

def two_opt_swap(route, i, k):
    return route[:i] + route[i:k+1][::-1] + route[k+1:]

def variable_neighborhood_descent(solution):
    improved = True
    best_solution = solution
    best_cost = calculate_tour_cost(solution)
    
    while improved:
        improved = False
        for i in range(1, len(best_solution) - 2):
            for j in range(i+1, len(best_solution) - 1):
                if j - i == 1:
                    continue  # No need to swap adjacent elements
                new_solution = two_opt_swap(best_solution, i, j)
                new_cost = calculate_tour_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution
                    best_cost = new_cost
                    improved = True
    return best_solution

def gvns(k_max, max_iter):
    best_solution = create_initial_solution()
    best_cost = calculate_tour_cost(best_solution)
    for _ in range(max_iter):
        k = 1
        while k <= k_max:
            shaken_solution = shake(best_solution)
            new_solution = variable_neighborhood_descent(shaken_solution)
            new_cost = calculate_tour_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
                k = 1  # Reset if improvement
            else:
                k += 1
    return best_solution, best_cost

# Run GVNS algorithm
best_tour, total_cost = gvns(k_max=3, max_iter=100)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")