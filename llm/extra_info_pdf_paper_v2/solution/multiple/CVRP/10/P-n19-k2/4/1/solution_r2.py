import numpy as np
import math

# Define city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Constants
num_robots = 2
robot_capacity = 160
depot = 0

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Compute savings
savings_list = []
for i in range(1, num_cities):
    for j in range(i + 1, num_cities):
        if i != j:
            saving = distance_matrix[depot][i] + distance_matrix[depot][j] - distance_matrix[i][j]
            savings_list.append((saving, i, j))
savings_list.sort(reverse=True, key=lambda x: x[0])

# Clarke-Wright algorithm to assign routes
tours = []
visited = set([depot])
capacity = {robot: robot_capacity for robot in range(num_robots)}
active_tour = {robot: [depot] for robot in range(num_robots)}

while savings_list and len(visited) < num_cities:
    _, i, j = savings_list.pop(0)
    if i in visited and j in visited:
        continue
    if i not in visited or j not in visited:
        target, new_city = (i, j) if i in visited else (j, i)
        for robot in range(num_robots):
            if sum(demands[city] for city in active_tour[robot]) + demands[new_city] <= capacity[robot]:
                active_tour[robot].append(new_city)
                visited.add(new_city)
                break

# Close all tours
for robot in range(num_robots):
    if active_tour[robot] and active_tour[robot][-1] != depot:
        active_tour[robot].append(depot)
    tours.append(active_tour[robot])

# Calculate tour costs
tour_costs = []
for tour in tours:
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    tour_costs.append(cost)

# Output results
overall_cost = sum(tour_costs)
for idx, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {idx % num_robots} Tour: {tour}")
    print(f"Robot {idx % num_robots} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")