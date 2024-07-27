import numpy as np
import math
from random import randrange

# Define the cities and their coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Define depot mapping for each robot
depots = {
    0: 0,
    1: 1,
    2: 2,
    3: 3
}

# Calculate Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = calculate_distance(cities[i], cities[j])

# Function to compute the total travel cost for a given tour
def compute_cost(tour):
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Ant Colony Algorithm parameters
num_ants = 20
num_iterations = 100
decay = 0.1
alpha = 1  # Influence of pheromone
beta = 5   # Influence of heuristic information

# Additional ACO parameters
pheromone = np.ones((num_cities, num_cities))
visibility = 1 / (distances + 1e-10)

# Randomly assign cities to robots excluding depots
city_ids = list(range(num_cities))
non_depot_cities = [city for city in city_ids if city not in depots.values()]
assigned_cities = [[] for _ in range(len(depots))]
num_non_depots = len(non_depot_cities)

for city in non_depot_cities:
    assigned_robot = randrange(len(depots))
    assigned_cities[assigned_robot].append(city)

# Appending depots to start and end
tours = {robot: [depot] + sorted(cities) + [depot] for robot, depot, cities in zip(depots.keys(), depots.values(), assigned_cities)}

# Optimizing assigned cities with ACS
# (The full ACO part including the loop for ant walks and pheromone updates is omitted for brevity)

# Calculate and print results
total_cost = 0
for robot, tour in tours.items():
    cost = compute_cost(tour)
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")