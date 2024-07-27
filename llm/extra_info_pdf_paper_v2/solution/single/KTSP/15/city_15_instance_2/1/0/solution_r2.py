import numpy as as np
import random

# Define the cities and their coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 
    11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Compute total travel cost for a tour
def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calc_distance(tour[i], tour[i + 1])
    return cost

# Generate initial solution
def generate_initial_solution(num_cities, total_required):
    selected_cities = random.sample(range(1, num_cities), total_required - 1)
    selected_cities = [0] + selected_cities + [0]  # Start and end at the depot
    return selected_cities

# Local search strategy using swapping
def local_search_swap(tour):
    best_tour = tour[:]
    best_cost = total_tour_cost(tour)
    
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_cost = new_cost
                    improved = True
    return best_tour

# General Variable Neighborhood Search (GVNS) for k-TSP
def gvns_ktsp(k):
    current_tour = generate_initial_solution(len(cities), k)
    current_cost = total_tour_cost(current_tour)
    
    stopping_condition = 0
    while stopping_condition < 50:
        new_tour = local_search_swap(current_tour)
        new_cost = total_tour_cost(new_tour)
        if new_cost < current_cost:
            current_tour = new_tour[:]
            current_cost = new_cost
            stopping_condition = 0  # reset if improvement is found
        else:
            stopping_condition += 1
        
    return current_tour, current_cost

# Define the number of cities to be visited (k value)
selected_k = 8
final_tour, final_cost = gvns_ktsp(selected_k)
final_cost_rounded = round(final_cost, 2)

# Print the final tour and the total travel cost
print("Tour:", final_tour)
print("Total travel cost:", final_cost_rounded)