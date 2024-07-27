import math
from itertools import permutations

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Coordinates and demands of cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and their capacity
num_robots = 2
robot_capacity = 160

# Distance matrix calculation
n = len(coordinates)
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Split cities into manageable tours for each robot considering capacity constraints
# This function does not ensure optimal paths and distribution. It's a simple heuristic to get a feasible solution.
def create_tours(demands, capacity):
    remaining_demand = demands[:]
    tours = []
    while sum(remaining_demand) > 0:
        tour = [0]  # start at depot
        current_load = 0
        for city in range(1, len(remaining_demand)):
            if remaining_demand[city] > 0 and (current_load + remaining_demand[city]) <= capacity:
                tour.append(city)
                current_load += remaining_demand[city]
        for city in tour:
            if city != 0:
                remaining_demand[city] = 0
        tour.append(0)  # return to depot
        tours.append(tour)
    return tours

# Simple function to associate tours to robots
def assign_tours_to_robots(tours, num_robots):
    robot_tours = [[] for _ in range(num_robots)]
    for i, tour in enumerate(tours):
        robot_tours[i % num_robots].append(tour)
    return robot_tours

# Calculate the total travel cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    return cost

# Generate initial tours
initial_tours = create_tours(demands, robot_capacity)

# Assign tours to each robot
robot_tours = assign_tours_to_robots(initial_tours, num_robots)

# Calculate and print the results
overall_total_cost = 0
for i, tours in enumerate(robot_tours):
    total_cost = sum(calculate_tour_cost(tour, distance_matrix) for tour in tours)
    overall_total_cost += total_hzcost
    for tour in tours:
        print(f"Robot {i} Tour: {tour}")
        print(f"Tour Cost: {calculate_tour_cost(tour, distance_matrix)}")
    print(f"Robot {i} Total Travel Cost: {total_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")