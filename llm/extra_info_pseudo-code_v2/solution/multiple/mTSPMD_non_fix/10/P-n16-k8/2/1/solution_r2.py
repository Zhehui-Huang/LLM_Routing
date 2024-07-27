import numpy as np
from scipy.spatial.distance import euclidean
import random

# City coordinates configuration
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}
num_robots = 8
start_depot = 0

# Calculate the Euclidean distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

dist_matrix = calculate_distance_matrix(cities)

# Divide the cities fairly among robots
city_indices = list(cities.keys())
city_indices.remove(start_depot)  # Remove depot from the list to distribute the rest
random.shuffle(city_indices)  # Randomize to simulate initial population diversity
partition_size = len(city_Indices) // num_robots
tours = [city_indices[i * partition_size:(i + 1) * partition_size] for i in range(num_robots)]

# Ensure each robot starts from the depot and calculates the tour completion by going back to depot
for tour in tours:
    tour.insert(0, start_depot)  # Start from depot
    tour.append(start_depot)  # Optionally, end at depot (can be modified depending on problem statement)

# Calculate costs
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

tour_costs = [calculate_tour_cost(tour, dist_matrix) for tour in tours]
overall_cost = sum(tour_costs)

# Display results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print("Overall Total Travel Cost:", overall_cost)