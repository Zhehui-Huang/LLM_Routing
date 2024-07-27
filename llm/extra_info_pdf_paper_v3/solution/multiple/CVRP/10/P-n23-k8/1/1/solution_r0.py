import math
from collections import defaultdict

# Cities and their coordinates (Index associated with each city)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Demand for each city
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Number of robots and their capacity
num_robots = 8
robot_capacity = 40

# Function to calculate Euclidean distance between two points
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix creation
dimension = len(coordinates)
dist_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(dimension)] for i in range(dimension)]

# Base structure for holding the tours
tours = defaultdict(list)
for i in range(num_robots):
    tours[i].append(0)  # each tour starts at the depot

# First heuristic attempt: Greedy distribution based on nearest neighbor which respects demand and capacity constraints
def nearest_neighbor_tours():
    global tours
    unvisited = set(range(1, dimension))
    loads = [0] * num_robots
    remaining_capacities = [robot_capacity] * num_robots
    
    while unvisited:
        for robot in range(num_robots):
            if not unvisited:
                break
            current_city = tours[robot][-1]
            next_city = None
            min_distance = float('inf')
            for city in unvisited:
                if (dist_matrix[current_city][city] < min_distance and
                    demands[city] <= remaining_capacities[robot]):
                    next_city = city
                    min_distance = dist_matrix[current_city][city]
            if next_city is not None:
                tours[robot].append(next_city)
                remaining_capacities[robot] -= demands[next_city]
                unvisited.remove(next_city)
    
    # Close the tours back to the depot
    for robot in range(num_robots):
        tours[robot].append(0)

nearest_neighbor_tours()

# Calculate tour costs
total_cost = 0
for robot in range(num_robots):
    tour_cost = sum(dist_matrix[tours[robot][i]][tours[robot][i+1]] for i in range(len(tours[robot])-1))
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost:.2f}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")