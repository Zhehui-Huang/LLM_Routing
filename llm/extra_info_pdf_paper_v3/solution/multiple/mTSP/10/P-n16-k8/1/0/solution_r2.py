import numpy as np
import random
from scipy.spatial import distance

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    coord1 = cities[city1]
    coord2 = cities[city2]
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Generate initial solutions with random tours
def generate_initial_solution():
    city_indices = list(cities.keys())[1:]  # Exclude depot city 0
    random.shuffle(city_indices)
    parts = np.array_split(city_indices, num_robots)
    return [[0] + part.tolist() + [0] for part in parts]

# Calculate the total travel cost for tours
def calculate_total_cost(tours):
    total_cost = 0
    individual_costs = []
    for tour in tours:
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        individual_costs.append(cost)
        total_cost += cost
    return total_cost, individual_costs

# Define number of robots
num_robots = 8

# Main optimization routine (simplified)
def optimize_tours():
    best_tours = generate_initial_solution()
    best_total_cost, best_individual_costs = calculate_total_cost(best_tours)
    
    # Attempt to find a better configuration (simple iteration example, can be replaced by a more sophisticated method)
    for _ in range(1000):
        new_tours = generate_initial_solution()
        new_total_cost, new_individual_costs = calculate_total_cost(new_tours)
        if new_total_cost < best_total_cost:
            best_tours = new_tours
            best_total_cost = new_total_cost
            best_individual_costs = new_individual_costs
    
    return best_tours, best_total_cost, best_individual_costs

# Find the optimal tours and costs
optimized_tours, overall_total_cost, individual_costs = optimize_tours()

# Outputting the results
for idx, (tour, cost) in enumerate(zip(optimized_tours, individual_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")