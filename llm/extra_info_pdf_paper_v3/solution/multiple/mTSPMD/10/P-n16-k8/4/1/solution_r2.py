import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define city coordinates and depot assignments
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Deploying robots
depots = {i: i for i in range(8)}  # Assuming depots from 0 to 7

# Fitness calculation based on total travel distance
def calculate_total_distance(tours):
    total_distance = 0
    detailed_costs = []
    for tour in tours:
        tour_distance = sum(euclidean(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        total_distance += tour_distance
        detailed_costs.append((tour, tour_distance))
    return total_distance, detailed_costs

# Generate initial solution
def generate_initial_solution():
    non_depot_cities = list(set(cities.keys()) - set(depots.keys()))
    random.shuffle(non_depot_cities)
    tours = [[depot] for depot in depots.values()]
    for i, city in enumerate(non_depot_cities):
        tours[i % len(tours)].extend([city, tours[i % len(tours)][0]])
    return tours

# Perform the genetic algorithm
def genetic_algorithm(max_generations=500):
    current_solution = generate_initial_solution()
    best_distance, best_solution_details = calculate_total_distance(current_solution)
    
    for generation in range(max_generations):
        # Create new solutions by swapping two cities in two tours
        new_solution = [tour[:] for tour in current_solution]  # deep copy to avoid mutation issues
        tour1, tour2 = random.sample(range(len(new_solution)), 2)
        city1, city2 = random.randint(1, len(new_solution[tour1]) - 2), random.randint(1, len(new_solution[tour2]) - 2)
        # Swap cities
        new_solution[tour1][city1], new_solution[tour2][city2] = new_solution[tour2][city2], new_solution[tour1][city1]
        
        # Calculate new distance
        new_distance, new_solution_details = calculate_total_distance(new_solution)
        
        # Selection: if the new solution is better, accept it
        if new_distance < best_distance:
            best_distance = new_distance
            best_solution_details = new_solution_details
            current_solution = new_solution  # update with the better solution

    return best_distance, best_solution_details

# Run Genetic Algorithm
best_distance, best_solution_details = genetic_algorithm()

# Outputs
print(f"Overall Total Travel Cost: {best_distance}")
for tour, cost in best_solution_details:
    print(f"Tour: {tour}")
    print(f"Total Travel Cost: {cost}")