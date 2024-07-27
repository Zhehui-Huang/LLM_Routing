import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# Cities' coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
])

# Calculate the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

def get_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += dist_matrix[tour[i], tour[i + 1]]
    return cost

# Generate optimal partition of cities for the robots minimizing combined travel
# since problem is NP-hard, we use a naive approach here (not scalable for large number of cities)
min_total_cost = float('inf')
best_tours = None

for split in range(2, len(coordinates) - 1):
    cities = list(range(2, len(coordinates)))
    for perm in permutations(cities):
        tour1 = [0] + list(perm[:split])
        tour2 = [1] + list(perm[split:])

        tour1_cost = get_tour_cost(tour1)
        tour2_cost = get_tour_cost(tour2)

        total_cost = tour1_cost + tour2_cost

        if total_cost < min_total_cost:
            min_total_cost = total_cost
            best_tours = (tour1, tour2, tour1_cost, tour2_cost)

# Output the results
robot_0_tour, robot_1_tour, robot_0_cost, robot_1_cost = best_tours

print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
print("")

print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}")
print("")

print(f"Overall Total Travel Cost: {robot_0_cost + robot_1_cost}")