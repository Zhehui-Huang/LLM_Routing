import numpy as np
from itertools import permutations

# Define a function to compute the cost of a given tour
def compute_cost(tour, distance_matrix):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i-1]][tour[i]]
    return cost

# Select the best tour among permutations within selected cities
def best_tour_among_permutations(selected_cities, distance_matrix):
    lowest_cost = float('inf')
    best_tour = None
    for perm in permutations(selected_cities):
        tour_cost = compute_cost(perm, distance_matrix)
        if tour_cost < lowest_cost:
            lowest_cost = tour_cost
            best_tour = perm
    return best_tour, lowest_cost

def k_tsp_solver(distance_matrix, start_city, k=12):
    num_cities = len(distance_matrix)
    all_cities = set(range(num_cities))
    
    # Ensure the starting city is in the tour
    selected_cities = [start_city]
    other_cities = list(all_cities - {start_city})
    
    # Choose (k-1) additional cities randomly
    np.random.seed()
    selected_cities.extend(np.random.choice(other_cities, k-1, replace=False))
    
    best_overall_tour = None
    best_overall_cost = float('inf')
    
    # Multistart loop to find best solution
    for _ in range(100):  # Number of restarts; this can be adjusted for trade-off performance
        np.random.shuffle(selected_cities)
        tour, cost = best_tour_among_permutations(selected_cities + [start_city], distance_metric)
        
        if cost < best_overall_cost:
            best_overall_tour = tour
            best_overall_cost = cost
    
    # Ensure the tour starts and ends at the depot city
    if best_overall_tour[0] != start_city:
        # Rotate tour to start at the depot city
        start_index = best_overall_tour.index(start_city)
        best_overall_tour = best_overall_tour[start_index:] + best_overall_tour[:start_index]
    best_overall_tour.append(start_city)

    return best_overall_tour, best_overall_cost

# Solving the k-TSP
tour_result, total_cost = k_tsp_solver(distance_matrix, 0)
print(f"Tour: {tour_result}")
print(f"Total travel cost: {total_cost:.2f}")