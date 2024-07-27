import numpy as np
from scipy.spatial.distance import euclidean
from copy import deepcopy
import random

# City coordinates definition (City index corresponds to position in the list)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Robots info
num_robots = 2
depot = coordinates[0]  # index 0

# Calculate distance matrix
n = len(coordinates)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = euclidean(coordinates[i], coordinates[j])

# Function to calculate the travel cost of the entire tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i], tour[i + 1]]
    return total_cost

# Initial solution
def initialization():
    tours = [[] for _ in range(num_robots)]
    # Start each tour at the depot and add first closest city separately
    sorted_cities = sorted(range(1, n), key=lambda x: distance_matrix[0, x])
    for i in range(num_robots):
        tours[i].append(0)
        tours[i].append(sorted_cities.pop(0))

    # Greedily assign remaining cities to minimize max tour length
    while sorted_cities:
        min_tour_idx = -1
        min_increase = float('inf')
        for city in sorted_cities:
            for i in range(num_robots):
                cost_if_added = calculate_tour_cost(tours[i] + [city, 0]) - calculate_tour_cost(tours[i] + [0])
                if cost_if_added < min_increase:
                    min_increase = cost_if_added
                    min_city = city
                    min_tour_idx = i

        tours[min_tour_idx].append(min_city)
        sorted_cities.remove(min_city)

    # Close all tours at the depot
    for i in range(num_robots):
        tours[i].append(0)

    return tours

# Final solution after initialization
tours = initialization()
tour_costs = [calculate_tour_cost(tour) for tour in tours]
max_cost = max(tour_costs)

# Print the output
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")