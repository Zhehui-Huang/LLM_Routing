import numpy as np
import random

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Basic problem parameters
num_robots = 8
depots = list(range(num_robots))  # Depots are the first `num_robots` entries in cities

def distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Ant Colony Optimization Parameters
n_iterations = 50
n_ants = 20
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5
pheromones = [[1 for _ in range(len(cities))] for _ in range(len(cities))]

def ant_colony_optimization():
    best_solution_cost = float('inf')
    best_solution = None

    for iteration in range(n_iterations):
        # Generate solutions
        for _ in range(n_ants):
            tours = []
            solution_cost = 0
            remaining_cities = set(cities.keys()) - set(depots)

            # Create tours for each robot starting from a depot
            for depot in depots:
                tour = [depot]
                current_city = depot
                
                while remaining_cities:
                    next_city = min(remaining_cities, key=lambda x: distance(current_city, x) * (pheromones[current_city][x] ** -alpha))
                    tour.append(next_city)
                    remaining_cities.remove(next_city)
                    current_city = next_city

                # Close the tour by returning to the depot
                tour.append(depot)
                tours.append(tour)
                
                # Calculate tour cost
                tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
                solution_cost += tour_cost

            # Pheromone update
            for tour in tours:
                for j in range(len(tour) - 1):
                    pheromones[tour[j]][tour[j + 1]] *= (1 - evaporation_rate)
                    pheromones[tour[j]][tour[j + 1]] += 1.0 / solution_cost

            # Track the best solution
            if solution_cost < best_solution_cost:
                best_solution_cost = solution_cost
                best_solution = tours

    return best_solution, best_solution_cost

best_tours, best_cost = ant_colony_optimization()

# Formatting results
overall_total_cost = 0
for idx, tour in enumerate(best_tours):
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")