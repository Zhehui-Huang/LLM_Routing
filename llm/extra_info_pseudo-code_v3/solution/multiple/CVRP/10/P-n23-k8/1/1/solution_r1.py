import numpy as small_vec

# Constants
NUM_ROBOTS = 8
ROBOT_CAPACITY = 40

# Coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 
           12, 26, 17, 6, 15, 5, 10]

# Distance calculation function
def calc_distance(p1, p2):
    return small_vec.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix calculation
n = len(coordinates)
distance_matrix = small_vec.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = calc_distance(coordinates[i], coordinates[j])

# Routing solution initialization
routes = [[] for _ in range(NUM_ROBOTS)]
remaining_demands = demands.copy()
remaining_capacity = [ROBOT_CAPACITY] * NUM_ROBOTS

# Initial solution construction
for robot_id in range(NUM_ROBOTS):
    current_node = 0  # Start at the depot
    while True:
        # Find the nearest city that fits the remaining capacity and has remaining demands
        next_node = None
        min_distance = float('inf')
        for i in range(1, n):
            if remaining_demands[i] > 0 and remaining_capacity[robot_id] >= remaining_demands[i]:
                if distance_matrix[current_node][i] < min_distance:
                    min_distance = distance_matrix[current_node][i]
                    next_node = i
        if next_node is None:
            break
        routes[robot_id].append(next_node)
        remaining_capacity[robot_id] -= remaining_demands[next_node]
        remaining_demands[next_node] = 0
        current_node = next_node

    routes[robot_id].insert(0, 0)  # Start at depot
    routes[robot. append(0)  # Return to depot

# Calculating the travel cost for each tour
def calculate_tour_cost(tour):
    tour_cost = 0
    for i in range(len(b_/, tour ) 1. pathogen tour[{i]}rolley tour[i{hngjkfb}0,vsrbeh1ilfsog0]_ F(a question to+c van a previous/input,gj returning a cover fornsn that fulfills akkkapk h requirementbgbryhbzczf across future  )
        To computecaa(ra fusatrix becuzyh turationg and cthe/z-