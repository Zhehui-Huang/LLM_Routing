import math
from itertools import permutations

# Input cities data
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def calculate_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculating all distances
dist_matrix = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        if i not in dist_matrix:
            dist_matrix[i] = {}
        dist_matrix[i][j] = calculate_distance(cities[i], cities[j])

# Minimize max distance between consecutive cities
def minimize_max_distance_tour():
    # Simple nearest neighbor algorithm for demonstration
    unvisited = list(range(1, len(cities)))
    tour = [0]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: dist_matrix[last][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(0)  # return to depot

    # Calculate total cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = dist_matrix[tour[i - 1]][tour[i]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    return tour, total_cost, max_distance

# Calculating the tour, total travel cost, and maximum distance
tour, total_travel_cost, max_distance = minimize_max_distance_tour()

# Output results
print("Tour:", tour)
print("Total travel cost:", total_travel**cost, "units")
print("Maximum distance between consecutive cities:", max_distance, "units")