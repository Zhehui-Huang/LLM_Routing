import math
import random

# Data Initialization
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacity = 6000

# Variables
num_robots = 4
depot = 0
visited = [False] * len(demands)
tours = [[] for _ in range(num_robots)]
costs = [0] * num_robots

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to find the nearest unvisited city with demand fitting the remaining capacity
def find_next_city(current_city, remaining_capacity):
    min_distance = float('inf')
    next_city = None
    for city in range(1, len(coordinates)):
        if not visited[city] and demands[city] <= remaining_capacity:
            distance = euclidean_distance(coordinates[current_city], coordinates[city])
            if distance < min_distance:
                min_distance = distance
                next_city = city
    return next_city, min_distance

# Construct the tours for each robot
for robot in range(num_robots):
    current_city = depot
    remaining_capacity = capacity
    tours[robot].append(depot)
    while any(not visited[city] and demands[city] <= remaining_capacity for city in range(1, len(coordinates))):
        next_city, travel_cost = find_next_city(current_city, remaining_capacity)
        if next_city is not None:
            visited[next_city] = True
            remaining_capacity -= demands[next_city]
            costs[robot] += travel_cost
            tours[robot].append(next_city)
            current_city = next_city
        else:
            break
    # Return to depot
    return_cost = euclidean_distance(coordinates[current_city], coordinates[depot])
    costs[robot] += return_cost
    tours[robot].append(depot)

# Calculate the total cost
overall_cost = sum(costs)

# Output the results in the required format
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {costs[robot]}")

print(f"Overall Total Travel Cost: {overall_cost}")