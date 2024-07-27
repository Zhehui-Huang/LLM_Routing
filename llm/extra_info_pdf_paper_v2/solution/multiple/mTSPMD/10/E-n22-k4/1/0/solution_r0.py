import numpy as np
import math

# Calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.dist(coord1, coord2)

# Setup cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}
num_cities = len(cities)

# Indices of depots for each robot
depots = {
    0: 0,
    1: 1,
    2: 2,
    3: 3
}

# Number of robots
num_robots = 4

# Initialize the distance matrix
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')  # Infinite distance to self

# Placeholder - Ant Colony Optimization for the mTSP with multiple depots
def ant_colony_optimization():
    # Placeholder for ACO algorithm implementation
    global distances
    import random
    
    # As an example, random greedy approach (not ACO):
    visited = set()
    tours = {}
    costs = {}
    tour_costs = []

    for robot in range(num_robots):
        current_city = depots[robot]
        tour = [current_city]
        total_cost = 0
        
        cities_to_visit = list(set(range(num_cities)) - set(depots.values()) - visited)
        random.shuffle(cities_to_visit)
        
        while cities_to_visit:
            next_city = min(cities_to_visit, key=lambda x: distance_matrix[current_city][x])
            if next_city not in visited:
                tour.append(next_city)
                total_cost += distance_matrix[current_city][next_city]
                current_city = next_city
                visited.add(next_city)
        
        tour.append(depots[robot])
        total_cost += distance_matrix[current_city][depots[robot]]
        tours[robot] = tour
        costs[robot] = total_cost
        tour_costs.append(total_cost)
    
    overall_cost = sum(tour_costs)
    return tours, costs, overall_cost

# Solve the problem
tours, costs, overall_cost = ant_colony_optimization()

# Display the results
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[ robot]}")
    print(f"Robot {robot} Total Travel Cost: {costs[robot]}")

print(f"Overall Total Travel Cost: {overall_cost}")