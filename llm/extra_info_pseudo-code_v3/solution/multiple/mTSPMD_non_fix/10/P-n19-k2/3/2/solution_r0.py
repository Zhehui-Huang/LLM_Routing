import math
import numpy as np
from itertools import permutations

# Given cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialization by Nearest Neighbor Search (NNS)
def initialize_tours():
    unvisited = list(cities.keys())[1:] # Exclude the starting depot
    tours = {0: [0], 1: [0]} # Starting from depot city 0 for both robots
    while unvisited:
        for robot_id in tours:
            if not unvisited:
                break
            # Find nearest city from the last city in the current tour
            last_city = tours[robot_id][-1]
            nearest_city = min(unvisited, key=lambda city: distance(last_city, city))
            tours[robot_id].append(nearest_city)
            unvisited.remove(nearest_city)
    # Ending at any city, no need to return to depot
    return tours

# Calculate the total travel cost of a tour
def calculate_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance(tour[i - 1], tour[i])
    return cost

# Main Tabu Search Algorithm (simplified for demonstration)
def tabu_search(tours, iterations=100, patience=20):
    best_solution = tours.copy()
    best_cost = sum(calculate_cost(tour) for tour in best_solution.values())

    current_solution = best_solution.copy()
    current_cost = best_cost
    no_improve = 0

    while iterations > 0 and no_improve < patience:
        # Here one could perform move operations: relocate, exchange, etc.
        # For brevity, a simple local swap is demonstrated within tours
        for robot_id, tour in current_solution.items():
            for i in range(1, len(tour) - 1):
                for j in range(i + 1, len(tour)):
                    # Swap cities and calculate new cost
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_cost = calculate_cost(new_tour)
                    if new_cost < current_cost:
                        current_solution[robot_id] = new_tour
                        current_cost = sum(calculate_cost(t) for t in current_solution.values())
                        if current_cost < best_cost:
                            best_solution = current_solution.copy()
                            best_cost = current_cost
                            no_improve = 0
                        break
                else:
                    continue
                break
        iterations -= 1
        no_improve += 1

    return best_solution

# Initialize tours
initial_tours = initialize_tours()
# Improve tours using Tabu Search
improved_tours = tabu_search(initial_tours)

# Calculate costs
total_cost = 0
for robot_id, tour in improved_tours.items():
    tour_cost = calculate_cost(tour)
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")