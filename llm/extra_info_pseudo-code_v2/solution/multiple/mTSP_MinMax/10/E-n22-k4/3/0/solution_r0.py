import math
import random

# Cities coordinates where the first element is the depot
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Initialize the tours for the robots, starting at the depot
num_robots = 4
tours = {i: [0] for i in range(num_robots)}

# Simple initialization of the tours (greedy nearest neighbor)
unvisited_cities = list(range(1, len(cities)))
random.shuffle(unvisited_cities)

for city in unvisited_cities:
    # Assign city to the shortest current tour
    min_tour_length = float('inf')
    best_robot = None
    for robot in range(num_robots):
        current_length = sum(distance(cities[tours[robot][i]], cities[tours[robot][i + 1]]) for i in range(len(tours[robot]) - 1))
        if current_length < min_tour_length:
            min_tour_length = current_tour_length
            best_robot = robot
    tours[best_robot].append(city)

# Make sure all tours end at the initial position (depot)
for robot in range(num_robots):
    tours[robot].append(0)

# Calculate the cost of each tour
def calculate_tour_cost(tour):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

tour_costs = {robot: calculate_tour_cost(tours[robot]) for robot in range(num_robots)}

# Find the maximum travel cost among all tours
max_cost = max(tour_costs.values())

# Output the solution
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tour_costs[robot]}")

print(f"Maximum Travel Cost: {max_cost}")