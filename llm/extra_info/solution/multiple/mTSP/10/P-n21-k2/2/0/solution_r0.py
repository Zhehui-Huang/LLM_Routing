import math
from itertools import permutations

# Coordinates of the cities (depot included at index 0)
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
          (62, 63), (63, 69), (45, 35)]

# Calculate Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = calculate_distance(cities[i], cities[j])
    return distance_matrix

distance_matrix = create_distance_matrix(cities)

# Define a simple yet effective way to split cities between robots
def heuristic_split(cities):
    # Using a simple longitude based split for a heuristic approach
    sorted_cities = sorted(list(enumerate(cities)), key=lambda x: x[1][0])  # Sort by x-coordinate
   
    # Divide the sorted list into two parts
    mid = len(sorted_cities) // 2
    robot_1_cities = sorted_cities[:mid]
    robot_2_cities = sorted_cities[mid:]
    
    return robot_1_cities, robot_2_cities

robot_1_cities, robot_2_cities = heuristic_split(cities[1:])  # we exclude the depot city here for splitting

# In order to include the depot city in tours
robot_1_cities = [0] + [idx + 1 for idx, _ in robot_1_cities]  # include depot city
robot_2_cities = [0] + [idx + 1 for idx, _ in robot_2_cities]  # include depot city

# Function to compute the tour cost
def compute_tour_cost(tour, distance_matrix):
    cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return cost

# Simplistic nearest neighbor heuristic for generating tour
def nearest_neighbor_tour(start_city, cities, distance_matrix):
    unvisited = cities.copy()
    tour = [start_city]
    current_city = start_city
    while len(unvisited) > 1:
        next_city = min((distance_matrix[current_city][i], i) for i in unvisited if i != current_city)[1]
        tour.append(next_city)
        unvisited.remove(current_city)
        current_city = next_city
    tour.append(start_city)  # return to depot
    return tour

# Generate tours
tour_1 = nearest_neighbor_tour(0, robot_1_cities, distance_matrix)
tour_2 = nearest_neighbor_tour(0, robot_2_cities, distance_matrix)

# Compute costs
cost_1 = compute_tour_cost(tour_1, distance_matrix)
cost_2 = compute_tour_cost(tour_2, distance_matrix)
total_cost = cost_1 + cost_2

# Output tour and cost information
print('Robot 0 Tour:', tour_1)
print('Robot 0 Total Travel Cost:', cost_1)
print()
print('Robot 1 Tour:', tour_2)
print('Robot 1 Total Travel Cost:', cost_2)
print()
print('Overall Total Travel Cost:', total