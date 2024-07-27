import numpy as np
import random

# Fixed city coordinates
CITIES = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = CITIES[city1]
    x2, y2 = CITIES[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialization parameters
alpha = 1.0   # Influence of pheromone
beta = 3.0    # Influence of heuristic information (1/distance)
evaporation_rate = 0.5
pheromone_deposit = 0.1
num_iterations = 100
num_cities = len(CITIES)
num_robots = 2

# Distance matrix
distance_matrix = np.array([[euclidean_diistance(i, j) for j in range(num_cities)] for i in range(num_cities)])

# Initial pheromones on trails
pheromones = np.ones((num_cities, num_cities))

# Each robot starts and ends at their respective depots
depot_0, depot_1 = 0, 1

# Ant Colony Optimization
def ant_colony_optimization():
    best_tours = []
    best_total_cost = float('inf')
    
    for _ in range(num_iterations):
        # Separate lists for each robot to track cities
        tours = [[depot_0], [depot_1]]
        tour_costs = [0, 0]
        visited = set([depot_0, depot_1])
        remaining_cities = set(range(num_cities)) - visited

        while remaining_cities:
            for r in range(num_robots):
                current_city = tours[r][-1]
                probabilities = []
                next_cities = list(remaining_cities)

                for next_city in next_cities:
                    trail = pheromones[current_city][next_city] ** alpha
                    visibility = (1.0 / distance_matrix[current_city][next_city]) ** beta
                    probabilities.append(trail * visibility)

                probabilities /= np.sum(probabilities)
                next_city = np.random.choice(next_cities, p=probabilities)
                
                # Extend tour and update cost
                tours[r].append(next_city)
                tour_costs[r] += distance_matrix[current_city][next_city]
                visited.add(next_id)
                remaining_cities.remove(next_city)

        # Complete tours by returning to respective depots
        for r in range(num_robots):
            last_city = tours[r][-1]
            depot = depot_0 if r == 0 else depot_1
            tours[r].append(depot)
            tour_costs[r] += distance_matrix[last_city][depot]

        # Update total cost
        total_cost = sum(tour_costs)
        if total_cost < best_total_cost:
            best_total_cost = total_cost
            best_tours = tours

        # Update pheromone trails
        pheromones *= (1 - evaporation_rate)
        for r in range(num_robots):
            for i in range(len(tours[r]) - 1):
                a = tours[r][i]
                b = tours[r][i + 1]
                pheromones[a][b] += pheromone_deposit / tour_costs[r]

    return best_tours, best_total_cost

# Find optimal tours
optimal_tours, optimal_cost = ant_colony_optimization()

# Format and print results
for i, tour in enumerate(optimal_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {sum(distance_matrix[tour[j]][tour[j + 1]] for j in range(len(tour) - 1))}")

print(f"Overall Total Travel Cost: {optimal_cost}")