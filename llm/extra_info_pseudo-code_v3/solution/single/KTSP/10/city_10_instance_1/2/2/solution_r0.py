import numpy as np
import random

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate a random initial solution
def generate_initial_solution(cities):
    tour = [0]  # starting and ending at the depot city
    available_cities = list(range(1, len(cities)))
    chosen_cities = random.sample(available_cities, 4)
    tour.extend(chosen_cities)
    tour.append(0)
    return tour

# Compute total distance of the tour
def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i], tour[i + 1]]
    return total_cost

# Shaking - simple swap of two non-depot cities
def shake(tour):
    a, b = random.sample(range(1, len(tour) - 1), 2)
    new_tour = tour[:]
    new_tour[a], new_tour[b] = new_tour[b], new_tour[a]
    return new_tour

# Variable Neighborhood Descent with swap (N2) only as simple VND method
def vnd(tour, distance_matrix):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour, distance_matrix)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if i != j:
                    new_tour = best_tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_cost = calculate_tour_cost(new_tour, distance_matrix)
                    if new_cost < best_cost:
                        best_tour = new_tour
                        best_cost = new_cost
                        improved = True
    return best_tour

# Define cities (x, y) coordinates
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

# Precompute the distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# GVNS parameters
Nrst = 50
best_solution = None
best_cost = float('inf')

# Run GVNS
for _ in range(Nrst):
    current_tour = generate_initial_solution(cities)
    current_cost = calculate_tour_cost(current_tour, distance_matrix)
    while True:
        new_tour = shake(current_tour)
        improved_tour = vnd(new_tour, distance_matrix)
        improved_cost = calculate_tour_cost(improved_tour, distance_matrix)
        if improved_cost < current_cost:
            current_tour = improved_tour
            current_cost = improved_cost
        else:
            break
    if current_cost < best_cost:
        best_solution = current_tour
        best_cost = current_cost

# Output the best solution and its cost
print("Tour:", best_solution)
print("Total travel cost:", best_cost)