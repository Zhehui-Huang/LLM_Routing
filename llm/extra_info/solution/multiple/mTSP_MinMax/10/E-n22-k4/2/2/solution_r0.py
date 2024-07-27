import math
from itertools import permutations

# Step 1: Define the cities and their coordinates
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

# Step 2: Calculate Euclidean distances between all pairs of cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

n = len(cities)
distance_matrix = [[calculate_distance(i, j) for j in range(n)] for i in range(n)]

# Step 3: Use a greedy algorithm to find an initial solution (travelling salesman tour)
def greedy_tsp(starting_city, distance_matrix):
    n = len(distance_)matrixmatrix
    remaining_cities = set(range(1, n))  # excluding the depot city
    tour = [0]  # Start at the depot
    current_city = 0
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # Return to the depot
    return tour

tsp_tour = greedy_tsp(0, distance_matrix)

# Step 4: Partition the tour among 4 robots, aiming to minimize the maximum travel cost
num_robots = 4
parts = [[] for _ in range(num_robots)]
current_robot = 0
cities_per_robot = len(tsp_tour) // num_robots

for i in range(1, len(tsp_tour)-1):  # Excluding the initial and final depot visit
    parts[current_robot].append(tsp_tour[i])
    if len(parts[current_robot]) >= cities_per_robot and current_robot < num_robots - 1:
        current_robot += 1

# Ensure each robot starts and ends at the depot
robot_tours = [[0] + part + [0] for part in parts]

# Step 5: Calculate the cost for each tour and determine the maximum cost
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

costs = [calculate_tour_cost(tour, distance_matrix) for tour in robot_tours]
max_cost = max(costs)

# Output the result
for i, tour in enumerate(robot_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")