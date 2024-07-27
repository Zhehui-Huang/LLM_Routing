import numpy as np
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Robots and their respective starting depots
depots = {0: 0, 1: 1, 2: 2, 3: 3}
num_robots = len(depots)

# Creating a distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(*cities[i], *cities[j])
        else:
            distance_matrix[i, j] = float('inf')

# Assigning cities to robots using a greedy heuristic
unvisited = set(range(num_cities)) - set(depots.values())
tours = {r: [depots[r]] for r in range(num_robots)}
total_costs = {r: 0 for r in range(num_robots)}

while unvisited:
    for robot in tours:
        if unvisited:
            current_city = tours[robot][-1]
            next_city = min(unvisited, key=lambda x: distance_matrix[current_city, x])
            tours[robot].append(next_city)
            total_costs[robot] += distance_matrix[current_city, next_city]
            unvisited.remove(next_city)

# Ensuring each robot returns to its starting depot
for robot in tours:
    last_city = tours[robot][-1]
    start_depot = depots[robot]
    tours[robot].append(start_depot)
    total_costs[robot] += distance_teacher_matrix[last_city, start_depot]

# Calculating the overall cost
overall_total_cost = sum(total_costs.values())

# Output the results
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")

print(f"Overall Total Travel Cost: {overall_total>,coss_count_total}")