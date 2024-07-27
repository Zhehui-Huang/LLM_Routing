import math
import itertools

# City coordinates, with City 0 being the depot
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Helper function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all permutations of the cities (excluding the depot city 0), and then add 0 to the start and end
perms = itertools.permutations(range(1, len(cities)))

best_tour = None
min_bottleneck = float('inf')
min_total_cost = float('inf')

# Iterate over each possible tour permutation
for perm in perms:
    tour = [0] + list(perm) + [0]
    # Calculate the total distance and the maximum distance between any two consecutive cities in the tour
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(tour[i], tour[i + 1])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Keep track of the tour with the minimal bottleneck that cycles back to the starting city
    if max_distance < min_bottleneck:
        min_bottleneck = max_distance
        min_total_cost = total_cost
        best_tour = tour

# Output the best tour found along with the total travel cost and maximum bottleneck distance
print("Tour:", best_tour)
print("Total travel cost:", round(min_total_cost, 2))
print("Maximum distance between consecutive cities:", round(min_bottleneck, 2))