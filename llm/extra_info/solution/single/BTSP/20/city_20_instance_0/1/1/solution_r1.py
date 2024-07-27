import math
from itertools import permutations

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Input cities' coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

# Create a matrix for storing distances between cities
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def find_optimal_tour():
    best_route = None
    min_max_distance = float('inf')
    total_routes_checked = 0

    # Generate all permutations of the city indices excluding the depot city
    for perm in permutations(range(1, len(cities))):
        # Calculate the route starting and ending at the depot (city 0)
        route = [0] + list(perm) + [0]
        max_dist_in_route = max(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
        total_dist = sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
        
        if max_dist_in_route < min_max_distance:
            min_max: distance = max_dist_in_route
            best_route = route
            best_total_dist = total_dist

        total_routes_checked += 1
        if total_routes_checked % 100000 == 0:
            print(f"Checked {total_routes_checked} routes...", end="\r")

    return best_route, best_total_dist, min_max_distance

tour, total_cost, max_consecutive_distance = find_optimal_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)