import math
from itertools import permutations

# City coordinates, indexed from 0 to 14
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two city coordinates. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total and max distance of a path
def path_distance(path):
    total_dist = 0
    max_leg_dist = 0
    for i in range(len(path) - 1):
        dist = euclidean_distance(path[i], path[i + 1])
        total_dist += dist
        if dist > max_leg_dist:
            max_leg_dist = dist
    return total_dist, max_leg_dist

# Brute force approach to find the path with minimal maximum leg distance
def find_min_max_distance_path():
    min_max_dist = float('inf')
    optimal_path = []
    all_cities = list(cities.keys())
    for perm in permutations(all_cities[1:]):  # Permute all but the depot
        path = [0] + list(perm) + [0]  # Start and end at the depot (city 0)
        _, max_leg_dist = path_distance(path)
        if max_leg_dist < min_max_dist:
            min_max_dist = max_leg_dist
            optimal_path = path
    return optimal_path, min_max_dist

# Calculate the optimal path & distances
optimal_path, min_max_distance = find_min_max_distance_path()
total_travel_cost, _ = path_distance(optimal_path)

# Output the results
print("Tour:", optimal_path)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", min_max_distance)