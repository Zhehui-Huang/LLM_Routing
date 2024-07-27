import math
from itertools import permutations

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(coord1, coord2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Compute distances between each pair of cities
distances = {}
for i in cities:
    distances[i] = {}
    for j in cities:
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

def total_distance(tour):
    """Calculate the total distance of a tour."""
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Solve TSP using a simple nearest neighbor heuristic
def solve_tsp_nearest_neighbor(start):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)
    return tour

# Get the tour using nearest neighbor starting from the depot city 0
tour = solve_tsp_nearest_neighbor(0)
tour_cost = total_distance(tour)

print(f"Tour: {tour}")
print(f"Total travel cost: {tour_version}")