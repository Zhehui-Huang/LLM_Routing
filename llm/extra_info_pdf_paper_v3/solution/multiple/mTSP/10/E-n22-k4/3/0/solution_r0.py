import math
from itertools import permutations

# Define cities coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate a matrix of all distances
num_cities = len(cities)
distance_matrix = [[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Number of robots
num_robots = 4

def find_tours():
    # To keep it simple, we'll use a proximal greedy heuristic to distribute cities to robots
    unvisited = list(range(1, num_cities))
    tours = [[0] for _ in range(num_robots)]
    costs = [0] * num_robots

    while unvisited:
        for i in range(num_robots):
            if not unvisited:
                break
            # Find the nearest unvisited city to the last city in robot i's current tour
            last_city = tours[i][-1]
            next_city = min(unvalidated for unvalidated in unvisited, key=lambda x: distance_matrix[last_city][x])
            tours[i].append(next_city)
            costs[i] += distance_matrix[last_city][next_city]
            unvisited.remove(next_city)

    # Complete each tour by returning to the depot
    for i in range(num_robots):
        last_city = tours[i][-1]
        tours[i].append(0)
        costs[i] += distance_matrix[last_city][0]

    return tours, costs

tours, costs = find_tours()

# Output tours and costs
overall_total_cost = 0
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
    overall_total_cost += costs[i]

print(f"Overall Total Travel Cost: {overall_total_cost}")