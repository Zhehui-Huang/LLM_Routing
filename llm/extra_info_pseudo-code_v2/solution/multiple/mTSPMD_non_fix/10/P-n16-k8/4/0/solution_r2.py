import numpy as np
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate Euclidean distance between two cities
def distance(ci, cj):
    return np.hypot(cities[ci][0] - cities[cj][0], cities[ci][1] - cities[cj][1])

# Generate random initial solution with each robot starting at depot city 0
def generate_initial_solution():
    all_cities = list(cities.keys())[1:]  # exclude the depot city 0
    random.shuffle(all_cities)
    parts = np.array_split(all_cities, num_robots)
    tours = [[0] + part.tolist() + [0] for part in parts]
    return tours

# Total travel cost for a set of tours
def evaluate_solution(tours):
    total_cost = 0
    individual_costs = []
    for tour in tours:
        tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        individual_costs.append((tour, tour_cost))
        total_cost += tour_cost
    return individual_costs, total_cost

num_robots = 8
best_solution = generate_initial_solution()
best_individual_costs, best_total_cost = evaluate_solution(best_solution)

# Output results
for idx, (route, cost) in enumerate(best_individual_costs):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Travel Cost: {best_total_cost}")