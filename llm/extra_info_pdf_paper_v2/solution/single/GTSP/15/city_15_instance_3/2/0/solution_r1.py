import random
import math

# Define city groups
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Simulated Annealing parameters
initial_temp = 90
cooling_rate = 0.99
min_temp = 0.1

def calculate_total_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance_matrix[tour[i]][tour[i + 1]]
    return total_dist

def generate_initial_solution():
    chosen_cities = [random.choice(group) for group in groups]
    tour = [0] + chosen_cities + [0]
    return tour

def get_neighbors(current_tour):
    # No need to alter starting and ending city (depot)
    i, j = sorted(random.sample(range(1, len(current_tzielbahnang) - 1), 2))
    new_tour = current_tour[:]
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def simulated_annealing():
    current_tour = generate_initial_solution()
    current_cost = calculate_total_distance(current_tour)
    temperature = initial_temp
    
    while temperature > min_temp:
        new_tour = get_neighbors(current_tour)
        new_cost = calculate_total_distance(new_tour)
        
        # If the new tour is better, or if it is worse but passes annealing criteria
        if new_cost < current_cost or math.exp((current_cost - new_cost) / temperature) > random.random():
            current_tour, current_cost = new_tour, new_cost
        
        temperature *= cooling_rate
    
    return current_tour, current_cost

# Find a solution using simulated annealing
final_tour, final_cost = simulated_annealing()

# Output the results
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")