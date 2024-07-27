import numpy as np
from math import sqrt

# Constants
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
depots = [0, 1, 2, 3, 4, 5, 6, 7]
depot_to_robots = dict(zip(depots, range(len(depots))))
num_cities = len(coordinates)

# Calculate distances between all pairs of cities
distances = [[sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2) for j in range(num_cities)] for i in range(num_cities)]

# Ant Colony Optimization parameters
pheromone = np.ones((num_cities, num_cities))
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5
pheromone_deposit = 0.1
num_ants = 20
iterations = 100

def choose_next_city(current_city, possible_cities, pheromone, desirability):
    pheromone_levels = pheromone[current_city][possible_cities]
    desirability_levels = desirability[current_city][possible_cities]
    probabilities = pheromone_levels ** alpha * desirability_levels ** beta
    probabilities /= probabilities.sum()
    return np.random.choice(possible_cities, p=probabilities)

# Main loop of ACO
best_solution = None
best_cost = float('inf')

for iteration in range(iterations):
    all_tours = []
    for ant in range(num_ants):
        tours = {r: [d] for d, r in depot_to_robots.items()}
        remaining_cities = set(range(num_cities)) - set(depots)
        
        while remaining_cities:
            for robot, tour in tours.items():
                if not remaining_cities:
                    break
                current_city = tour[-1]
                possible_cities = list(remaining_cities)
                next_city = choose_next_city(current_city, possible_cities, pheromone, desirability)
                tour.append(next_city)
                remaining_cities.remove(next_city)
        
        # Complete tours by returning to respective depots
        for robot, tour in tours.items():
            tour.append(tour[0])
        
        # Gather all tours for cost calculation
        all_tours.append(tours)
    
    # Evaluate and update pheromones
    for tours in all_tours:
        total_cost = 0
        for tour in tours.values():
            tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            total_cost += tour_cost
        
        if total_cost < best_cost:
            best_cost = total_cost
            best_solution = tours
        
        # Pheromone update
        for route in tours.values():
            for i in range(len(route) - 1):
                pheromone[route[i]][route[i + 1]] += pheromone_deposit / tour_cost
        
        # Evaporate pheromone
        pheromone *= (1 - evaporation_rate)

# Output results
for robot_id, tour in best_solution.items():
    route_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {best_cost}")