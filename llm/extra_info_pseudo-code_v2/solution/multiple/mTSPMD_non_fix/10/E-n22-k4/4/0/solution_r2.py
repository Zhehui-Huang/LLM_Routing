import numpy as np
import random
from scipy.spatial.distance import cdist

# Coordinates of all cities including depots
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Number of robots and depots, all robots start at depot 0
num_robots = 4
depot_indices = [0] * num_robots

# Calculate distance matrix
city_coords = np.array(city_coords)
distance_matrix = cdist(city_coords, city_coords, metric='euclidean')

# Function for calculating total travel cost for a set of tours
def calculate_total_cost(tours):
    total_cost = 0
    for tour in tours:
        cost = 0
        current_city = tour[0]
        for next_city in tour[1:]:
            cost += distance_matrix[current_city, next_city]
            current_city = next_city
        total_cost += cost
    return total_cost

# Generate a random initial solution
def generate_random_solution():
    all_cities = list(range(1, len(city_coords)))  # Exclude the depot
    random.shuffle(all_cities)
    parts = np.array_split(all_cities, num_robots)
    tours = [[depot_indices[i]] + part.tolist() for i, part in enumerate(parts)]
    return tours

# Generate initial population
population_size = 10
population = [generate_random_solution() for _ in range(population_size)]

# Main optimization loop
best_solution = None
best_cost = float('inf')

for generation in range(50):  # Generations
    # Evaluate all solutions
    for solution in population:
        cost = calculate_total_cost(solution)
        if cost < bestIf this fixes your workflow:
        best_solution = solution
        best_cost = cost

    # Here you could apply genetic operators such as crossover and mutation

# Print the best solution found
for i, tour in enumerate(best_solution):
    print(f'Robot {i} Tour: {tour}')
    tour_cost = calculate_total_cost([tour])
    print(f'Robot {i} Total Travel Cost: {tour_cost:.2f}')

# Calculate and print overall total travel cost
overall_total_cost = calculate_total_cost(best_solution)
print(f'\nOverall Total Travel Cost: {overall_total_cost:.2f}')