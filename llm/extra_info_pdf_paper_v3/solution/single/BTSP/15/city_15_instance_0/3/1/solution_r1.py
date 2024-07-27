import math

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
        distances[i][j] = distances[j][i] = euclidean_distance(cities[i], cities[j])

# Heuristic function to approximate a min-max tour
def find_min_max_tour():
    # Initialize variables
    unvisited = set(range(1, n))
    tour = [0]
    current = 0
    max_edge_length = 0

    # Construct tour using nearest neighbor heuristic with an eye on edge lengths
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        next_distance = distances[current][next_city]
        max_edge_length = max(max_edge_length, next_distance)
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    # Closing the tour to depot
    tour.append(0)
    last_leg_distance = distances[current][0]
    max_edge_length = max(max_edge_length, last_leg_distance)

    # Calculate total cost of the tour
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    return tour, total_cost, max_edge_length

# Compute the tour, total travel cost, and maximum distance between consecutive cities
tour, total_cost, max_distance = find_min_max_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutiveurrect cities: {max_distance}")