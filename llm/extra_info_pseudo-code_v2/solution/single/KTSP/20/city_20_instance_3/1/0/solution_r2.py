import numpy as np
import random

# Define city locations
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate the total travel cost of the tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Generate an initial solution at random
def generate_initial_solution(k=13):
    tour = [0]  # start at the depot
    available_cities = list(range(1, 20))
    while len(tour) < k:
        next_city = random.choice(available_cities)
        tour.append(next_city)
        available_cities.remove(next_city)
    tour.append(0)  # end at the depot
    return tour

# Local search to improve the tour
def local_search(tour):
    best_cost = calculate_cost(tour)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 0 and j != 0 :  # ensuring not swapping the depot
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_cost = calculate_cost(new_tour)
                    if new_cost < best_cost:
                        best_tour = new_tour[:]
                        best_cost = new_cost
                        improved = True
    return best_tour

# Perform the General Variable Neighborhood Search (GVNS)
def GVNS(k=13, itermax=100):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_cost(best_solution)
    
    for _ in range(itermax):
        current_solution = local_search(best_solution)
        current_cost = calculate_cost(current_latency)
        current_solution = local_search(current_solution)
        current_cost = calculate_cost(current_solution)
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
            
    return best_solution, best_cost

# Execute the GVNS algorithm
best_tour, total_cost = GVNS()
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))