import math
import numpy as np

# Cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Config
num_robots = 2
depot_city = 0

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Generate distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Function to find tours for two robots using a simple greedy algorithm
def solve_mTSP_greedy(distance_matrix, num_robots, num_cities, depot_city):
    tours = [[] for _ in range(num_robots)]
    visited = set([depot_city])
    tours_costs = [0] * num_robots
    
    for _ in range(num_cities - 1):
        for robot_id in range(num_robots):
            current_city = tours[robot_id][-1] if tours[robot_id] else depot_city
            next_city = None
            min_distance = float('inf')
            
            for city in range(num_cities):
                if city not in visited and distance_matrix[current_city][city] < min_distance:
                    next_city = city
                    min_distance = distance_matrix[current_city][city]
            
            if next_city is not None:
                tours[robot_id].append(next_city)
                visited.add(next_city)
                tours_costs[robot_id] += min_distance
    
    # Close the tours back to depot
    for robot_id in range(num_robots):
        last_city = tours[robot_id][-1]
        back_to_depot_cost = distance_matrix[last_city][depot_city]
        tours_costs[robot_id] += back_to_depot_cost
        tours[robot_id].append(depot_city)
    
    return tours, tours_costs

# Solve the mTSP
tours, tours_costs = solve_mTSP_greedy(distance_matrix, num_robots, num_cities, depot_city)

# Calculate total cost
total_cost = sum(tours_costs)

# Output the results
for robot in range(num_robots):
    print(f"Robot {robot} Tour: [{depot_city}, " + ", ".join(map(str, tours[robot])) + "]")
    print(f"Robot {robot} Total Travel Cost: {tours_costs[robot]}")
print(f"Overall Total Travel Cost: {total_cost}")