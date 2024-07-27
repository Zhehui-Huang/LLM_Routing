import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define the cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to compute the total distance of a tour
def tour_distance(tour, cities):
    return sum(euclidean(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Function to solve TSP using brute force permutations, acceptable for small sets
def solve_tsp_brute_force(city_indices):
    best_distance = float('inf')
    best_tour = None
    for perm in permutations(city_indices):
        current_tour = [0] + list(perm) + [0]  # tour starts and ends at depot city 0
        current_distance = tour_distance(current_tour, cities)
        if current_distance < best_distance:
            best_distance = current_distance
            best_tour = current_tour
    return best_tour, best_distance

# Assuming there are 2 robots, we evenly split cities by nearest-neighbour heuristics
num_robots = 2
city_indices = np.array(range(1, len(cities))) # excluding the depot

# Split city indices into two approximately equal groups
city_group_1 = city_indices[0:len(city_indices)//2]
city_group_2 = city_indices[len(city_indices)//2:]

# Calculate best tours for each robot
tour_1, cost_1 = solve_tsp_brute_force(city_group_1)
tour_2, cost_2 = solve_tsp_brute_force(city_group_2)
overall_cost = cost_1 + cost_2

# Outputting results
print(f"Robot 0 Tour: {tour_1}")
print(f"Robot 0 Total Travel Cost: {cost_1:.2f}")
print(f"Robot 1 Tour: {tour_2}")
print(f"Robot 1 Total Travel Cost: {cost_2:.2f}")
print(f"Overall Total Travel Cost: {overall_cost:.2f}")