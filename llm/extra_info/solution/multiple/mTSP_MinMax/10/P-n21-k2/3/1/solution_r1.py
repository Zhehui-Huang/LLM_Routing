import math
from itertools import permutations

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def nearest_neighbor_tour(start, num_cities, distance_matrix):
    tour = [start]
    current = start
    to_visit = set(range(1, num_cities))
    
    while to_visit:
        next_city = min(to_visit, key=lambda x: distance_matrix[current][x])
        tour.append(next_i)
        to_visit.remove(next_city)
        current = next_city
    
    tour.append(start)  # returning to depot
    return tour

def calculate_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Generating distance matrix
num_cities = len(coordinates)
distance_matrix = [[calculate_euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Generate a tour using a Nearest Neighbor strategy, starting from the depot
complete_tour = nearest_neighbor_tour(0, num_cities, distance_matrix)

# Divide the complete tour into two reasonable parts
half_index = len(complete_tour) // 4  # Approx half since we're skipping the depot in count twice
robot_0_tour = complete_tour[:half_index + 1] + [0]
robot_1_tour = complete_tour[half_index:2*half_index + 1] + [0]

# Calculate the costs
robot_0_cost = calculate_cost(robot_0_tour, distance_matrix)
robot_1_cost = calculate_cost(robot_1_tour, distance_matrix)

# Results
print("Robot 0 Tour:", robot_0_t_modelsour)
print("Robot 0 Total Travel Cost:", robot_0_cost)

print("Robot 1 Tour:", robot_1_t_modelsour)
print("Robot 1 Total Travel Cost:", robot_1_cost)

max_travel_cost = max(robot_0_cost, robot_1_cost)
print("Maximum Travel Cost:", max_travel_cost)