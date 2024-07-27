import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Compute the distance matrix
coordinates = np.array(list(cities.values()))
dist_matrix = distance_matrix(coordinates, coordinates)

# Assign cities to depots (naive clustering based on proximity)
depots = list(range(8))
city_clusters = {depot: [depot] for depot in depots}

# Remaining cities to be distributed among the depots
remaining_cities = set(range(8, 16))

for city in remaining_cities:
    nearest_depot = min(depots, key=lambda depot: dist_matrix[depot][city])
    city_clusters[nearest_depot].append(city)

# Function to calculate the total travel cost of a path
def calculate_cost(path):
    return sum(dist_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))

# Solve TSP for each robot starting and ending at their depot, visiting their cluster of cities
tours = {}
total_costs = {}

for robot_id, cities in city_clusters.items():
    # Include return to the starting depot
    cities.append(cities[0])
    best_path = None
    min_cost = float('inf')
    
    # Generate permutation to find the best tour
    for perm in permutations(cities[1:-1]):
        current_path = [cities[0]] + list(perm) + [cities[0]]
        cost = calculate_driven_cost(current_path)
        if cost < min_cost:
            min_cost = cost
            best_path = current_path
    
    tours[robot_id] = best_path
    total_costs[robot_id] = min_cost

# Output the results
overall_total_cost = 0
for robot_id in sorted(tours):
    tour_string = ' -> '.join(map(str, tours[robot_id]))
    print(f"Robot {robot_id} Tour: {tour_string}")
    print(f"Robot {robot_id} Total Travel Cost: {total_costs[robot_id]:.2f}")
    overall_total_cost += total_costs[robot_id]

print(f"Overall Total Travel Cost: {overall_total_calcost:.2f}")