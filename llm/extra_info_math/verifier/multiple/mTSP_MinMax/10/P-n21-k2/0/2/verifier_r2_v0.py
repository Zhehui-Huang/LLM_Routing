import numpy as np

def calculate_tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i], tour[i+1]]
    return cost

def is_unique_visitation(tours, num_cities):
    city_count = {i: 0 for i in range(num_cities)}
    for tour in tours:
        for city in tour[1:-1]:  # Do not consider the depot (start and end)
            city_count[city] += 1
    return all(count == 1 for count in city_count.values() if count != 0)

def check_flow_conservation(tours):
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False
    return True

def check_binary_assignment(tours, distance_matrix):
    for tour in tours:
        for i in range(len(tour) - 1):
            if distance_matrix[tour[i], tour[i+1]] == 0:
                return False
    return True

def node_positions_valid(tours, distance_matrix):
    for tour in tours:
        for i in range(1, len(tour) - 1):
            if distance_matrix[tour[i], tour[i+1]] < 0:
                return False
    return True

# Cities coordinates (Depot + 20 other cities)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Define distance matrix
n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))

# Calculate Euclidean distances
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i, j] = np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j]))

# Tours provided in the solution
robot_0_tour = [0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0]
robot_1_tour = [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]

# Gather all tours
tours = [robot_0_tour, robot_1_tour]

# Validate tours against requirements
if (is_unique_visitation(tours, n_cities) and
    check_flow_conservation(tours) and
    check_binary_assignment(tours, distance_start_matrix) and
    node_positions_valid(tours, distance_matrix)):
    print("CORRECT")
else:
    print("FAIL")