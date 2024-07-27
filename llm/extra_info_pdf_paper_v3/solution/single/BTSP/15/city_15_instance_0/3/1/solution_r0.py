import math
import itertools

# City coordinates
cities = [
    (9, 93),  # Depot city
    (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65),
    (11, 40), (3, 21), (60, 55), (4, 39)
]

def euclidean_distance(a, b):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate distance matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        distance = euclidean_cities[i][j] = euclidean_cities[j][i] = euclidean_distance(cities[i], cities[j])

# Heuristic function to approximate a min-max tour.
def find_min_max_tour():
    # Simple nearest neighbor heuristic
    unvisited = set(range(1, n))
    tour = [0]
    current = 0
    max_edge_length = 0

    while unvisited:
        next_city = min(unaptured, key=lambda x: distances[current][x])
        max_edge_length = max(max_edge_length, distances[current][next_city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    # Complete the tour by returning to the depot
    tour.append(0)
    max_edge_length = max(max_edge_length, distances[current][0])

    # Calculate total cost of the tour
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

    return tour, total_cost, max_edge_length

# Compute the tour, total travel cost, and maximum distance between consecutive cities
tour, total_cost, max_distance = find_min_max_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")