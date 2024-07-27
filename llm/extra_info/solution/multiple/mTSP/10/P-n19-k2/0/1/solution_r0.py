import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),  4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Create an array for the coordinates
coordinates = np.array(list(cities.values()))

# Calculate the distance matrix between each pair of cities
dist_matrix = distance_matrix(coordinates, coordinates)

def calculate_tour_cost(tour, dist_matrix):
    cost = dist_matrix[tour[-1]][tour[0]]  # Closing the tour
    for i in range(len(tour) - 1):
        cost += dist_matrix[tour[i]][tour[i + 1]]
    return cost

def solve_tsp(tour, dist_matrix):
    # Start from depot, find permutations of cities, end at depot
    best_tour = None
    best_cost = float('inf')
    cities_to_visit = tour[1:-1]
    for perm in permutations(cities_to_visit):
        perm_cost = calculate_tour_cost((0,) + perm + (0,), dist_matrix)
        if perm_cost < best_cost:
            best_cost = perm_cost
            best_tour = (0,) + perm + (0,)
    return best_tour, best_cost
   
# Divide the cities into two approximately equal groups for both robots
group1 = [1, 4, 6, 8, 10, 11, 12, 14]  # Cities managed by robot 0
group2 = [2, 3, 5, 7, 9, 13, 15, 16, 17, 18]  # Cities managed by robot 1

tour1, cost1 = solve_tsp([0] + group1 + [0], dist_matrix)
tour2, cost2 = solve_tsp([0] + group2 + [0], dist_matrix)

# Calculate the overall cost
overall_cost = cost1 + cost2

# Output the results
print(f"Robot 0 Tour: {tour1}")
print(f"Robot 0 Total Travel Cost: {cost1}\n")
print(f"Robot 1 Tour: {tour2}")
print(f"Robot 1 Total Travel Cost: {cost2}\n")
print(f"Overall Total Travel Cost: {overall_cost}")