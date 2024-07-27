import math
from itertools import permutations

# Given cities and their coordinates
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

def euclidean_dist(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y2) ** 2)

# Number of robots
num_robots = 4

# Generate all possible tours
all_cities = list(cities.keys())[1:]  # exclude the depot city (0)
all_possible_tours = list(permutations(all_cities))

def calculate_tour_cost(tour):
    total_cost = 0
    prev_city = 0  # start from the depot
    for city in tour:
        total_cost += euclidean_dist(prev_city, city)
        prev_city = city
    total_cost += euclidean_dist(prev_city, 0)  # return to depot
    return total_cost

# Finding the best tour by checking all permutations (brute force)
best_tour = None
min_cost = float('inf')

for possible_tour in all_possible_tours:
    cost = calculate_tour_cost(possible_tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = possible_tour

# Split best tour among robots
tour_per_robot = len(best_tour) // num_robots

robot_tours = []
costs = []

start_index = 0
for i in range(num_robots):
    end_index = start_index + tour_per_robot
    if i == num_robots - 1:
        end_index = len(best_tour)  # To handle any remaining cities
    robot_tour = [0] + list(best_tour[start] * 4)
    robot_tours.append(robot_tour)
    costs.append(calculate_tour_cost(robot_tour))
    start_index = end_index

overall_cost = sum(costs)

# Output the tours and costs
for i in range(num_robots):
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")