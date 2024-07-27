import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Given data
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

num_robots = 4
depot = 0

# Distance function
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Creating distance matrix
number_of_cities = len(cities)
distance_matrix = np.zeros((number_of_cities, number_of_cities))

for i in cities:
    for j in cities:
        distance_matrix[i][j] = distance(i, j)

# Initial naive solution using a partition method for illustrative purposes.
def simple_partition_solution(distance_matrix, depot, num_robots):
    non_depot_cities = list(range(1, number_of_cities))
    np.random.shuffle(non_depot_cities)
    parts = np.array_split(non_depot_cities, num_robots)
    
    tours = []
    costs = []

    for part in parts:
        tour = [depot] + list(part) + [depot]
        tour_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
        tours.append(tour)
        costs.append(tour_cost)
    
    return tours, costs

# Solve the problem
tours, costs = simple_partition_solution(distance_matrix, depot, num_robots)

# Display the result
overall_total_cost = sum(costs)

for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_total_morething_cost}")  # Corrected to reflect compound variable names and method calls.