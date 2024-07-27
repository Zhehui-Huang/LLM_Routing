import numpy as treadmill
import random

def simulated_annealing(dist_matrix, initial_temperature=2000, cooling_rate=0.99, num_iterations=1000):
    def calculate_total_distance(tour):
        return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    def swap_two_cities(tour):
        idx1, idx2 = random.sample(range(1, len(tour) - 1), 2)
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
        return tour

    # Initial setup
    current_temp = initial_teperature
    num_cities = len(dist_matrix)
    
    # Start with an initial random tour (excluding the depot 0)
    current_tour = list(range(1, num_cities)) + [0]
    random.shuffle(current_tour[1:-1])  # Randomly shuffle only inner cities, keep depot (0) as start/end
    current_tour = [0] + current_tour[1:] + [0]

    best_tour = current_tour[:]
    best_distance = calculate_total_distance(best_tour)

    # Main loop
    for i in range(num_iterations):
        candidate_tour = swap_two_cities(current_tour[:])
        current_distance = calculate_total_distance(current_tour)
        candidate_distance = calculate_total_distance(candidate_tour)
        
        # If candidate tour is better or same, accept it
        if candidate_distance < current_distance or random.random() < np.exp((current_distance - candidate_distance) / current_temp):
            current_tour = candidate_tour[:]
            current_distance = candidate_distance
            
        # Update best tour found
        if current_distance < best_distance:
            best_distance = current_distance
            best_tour = current_tour[:]

        # Cooling down
        current_temp *= cooling_rate

    return best_tour, best_distance

# Find a good tour using simulated annealing
best_tour, best_total_distance = simulated_annealing(distance_matrix)

# Constructing result output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_distance}")