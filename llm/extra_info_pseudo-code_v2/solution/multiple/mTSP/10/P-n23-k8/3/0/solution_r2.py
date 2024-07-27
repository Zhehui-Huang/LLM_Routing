import math
import numpy as np

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate distance matrix for all city pairs
def calculate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])
    return distance_medicate

# Function to find the nearest neighbor from the current city
def find_nearest_neighbor(city_index, city_list, distance_matrix):
    nearest = None
    min_distance = float('inf')
    for i in city_list:
        if i != city_index and distance_matrix[city_index][i] < min_distance:
            nearest = i
            min_distance = distance_matrix[city_index][i]
    return nearest, min_distance

# Generate initial tours by distributing cities to each robot
def initial_tours(number_of_robots, city_indices, depot_index, distance_matrix):
    tours = [[] for _ in range(number_of_robots)]
    remaining_cities = set(city_indices)
    
    # Initial city for each tour
    while remaining_cities:
        for tour in tours:
            if remaining_cities:
                next_city = remaining_cities.pop()
                tour.append(next_city)

    # Close the tours at the depot
    for tour in tours:
        tour.insert(0, depot_index)
        tour.append(depot_index)

    return tours

# Calculate the cost of a single tour
def tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

def mTSP(cities, number_of_robots):
    city_indices = list(range(1, len(cities)))  # Exclude the depot
    depot_index = 0
    distance_matrix = calculate_distance_matrix(cities)

    # Generate initial tours
    tours = initial_tours(number_of_robots, city_indices, depot_index, distance_matrix)

    # Calculate costs for each tour and overall cost
    total_cost = 0
    for i, tour in enumerate(tours):
        cost = tour_cost(tour, distance_matrix)
        total_cost += cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}\n")
    
    print(f"Overall Total Travel Cost: {total_cost}")

# Define cities with coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
          (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Specify the Number of Robots
number_of_robots = 8

# Call the mTSP Solver
mTSP(cities, number_of_robots)