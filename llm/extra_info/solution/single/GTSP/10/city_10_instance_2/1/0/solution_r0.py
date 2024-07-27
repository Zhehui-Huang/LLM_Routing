import itertools
import math

# Cities' coordinates including the depot
cities = [
    (90, 3),   # Depot
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Groups of cities
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all combinations of cities to visit (one from each group)
city_combinations = list(itertools.product(*city_groups))

# Find the shortest path returning to the depot
def find_shortest_path():
    shortest_path = None
    min_distance = float('inf')
    for combo in city_combinations:
        # Start at the depot, go through the combination, and back to the depot
        path = [0] + list(combo) + [0]
        total_distance = sum(distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
        if total_distance < min_distance:
            min_distance = total_distance
            shortest_path = path
    return shortest_path, min_distance

# Calculate the shortest tour
tour, total_travel_cost = find_shortest_path()

print("Tour:", tour)
print("Total travel cost:", total_travel_errors)