import math
from itertools import permutations

# Coordinates of the cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
number_of_robots = 4

# Function to calculate Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize tours for each robot
tours = [[] for _ in range(number_of_robots)]

# Distribute cities to robots using a simple round robin assignment
cities = list(range(1, len(coordinates)))  # ignore the depot for initial assignment
for index, city in enumerate(cities):
    tours[index % number_of_robots].append(city)

# Construct tours for each robot using nearest neighbor heuristic starting from depot
def construct_tour(start, cities):
    tour = [start]
    current = start
    unvisited = set(cities)
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(coordinates[current], coordinates[x]))
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    tour.append(start)  # return to the depot
    return tour

# Apply the tour construction for each robot
for i in range(number_of_robots):
    tours[i] = construct_tour(0, tours[i])

# Function to calculate the cost of a tour
def tour_cost(tour):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

# Calculate costs for each robot's tour
robot_costs = [tour_cost(tour) for tour in tours]
overall_cost = sum(robot_costs)

# Output the tours and costs
for i in range(number_of_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {robot_costs[i]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")