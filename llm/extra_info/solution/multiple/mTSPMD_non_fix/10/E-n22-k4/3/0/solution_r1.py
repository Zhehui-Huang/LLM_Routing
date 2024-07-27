import math
from itertools import permutations

# Given data
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

num_robots = 4
depots = [0, 1, 2, 3]

# Helpers
def calc_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Nearest Neighbor Heuristic for TSP
def nearest_neighbor(start_city, excluded_cities):
    unvisited = set(range(len(coordinates))) - excluded_cities
    tour = [start_city]
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda x: calc_distance(current_city, x))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    return tour

# Determining balanced tours for robots
overall_cost = 0
robot_tours = []
for i in range(num_robots):
    if i < len(depots):
        start_city = depots[i]
    else:
    	start_city = coordinates.index(min(coordinates, key=lambda x: calc_distance(depots[i], x)))
        
    tour = nearest_neighbor(start_city, set(depots) - {start_city})
    # Adjusted exclusion for more realistic follow through
    cost = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    robot_tours.append((tour, cost))
    overall_cost += cost

# Output results
for i, (tour, cost) in enumerate(robot_tours):
    print(f"Robot {i + 1} Tour: {tour}")
    print(f"Robot {i + 1} Total Travel Cost: {round(cost, 2)}")
print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")