import math
import random
from itertools import permutations

# Coordinates for each city, including the depot city (index 0)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Function to optimize tour using the 2-opt algorithm
def two_opt(tour, max_iterations=10000):   
    min_change = True
    while min_change and max_iterations > 0:
        min_change = False
        best_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour)):
                if j - i == 1: continue  # skip consecutive edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = sum(euclidean_distance(new_tour[k], new_tour[k+1]) for k in range(len(tour)-1))
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    min_change = True
        max_iterations -= 1
    return tour

# Divide cities into nearly equal clusters for each robot
def divide_cities(num_robots, cities):
    avg = len(cities) / float(num_robots)
    out = []
    last = 0
    while last < len(cities):
        out.append(cities[int(last):int(last + avg)])
        last += avg
    return out

# Cluster cities (excluding the depot) and assign to robots
num_robots = 4
cities = list(range(1, 22))  # City indices excluding the depot
clusters = divide_cities(num_robots, cities)
robot_tours = []

# Generate and optimize tours for each robot
for cluster in clusters:
    tour = [0] + cluster + [0]  # add the depot city at the start and end
    optimized_tour = two_opt(tour)
    robot_tours.append(optimized_tour)

# Calculate costs and determine max cost
costs = [sum(euclidean_distance(robot_tours[i][j], robot_tours[i][j + 1]) for j in range(len(robot_tours[i]) - 1)) for i in range(num_robots)]
max_cost = max(costs)

# Outputting results
for index, tour in enumerate(robot_tours):
    cost = costs[index]
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")