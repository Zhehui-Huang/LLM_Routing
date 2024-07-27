import math

# Define the coordinates of the cities (including the depot as city 0)
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50),
    (72, 90), (54, 46), (8, 70), (97, 62),
    (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Initialize the distance matrix
n = len(coordinates)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def btsp_heuristic(start=0):
    """Heuristic to minimize the maximum distance between consecutive cities in the tour."""
    unvisited = set(range(1, n))
    tour = [start]
    current = start

    # Construct tour by always choosing the nearest unvisited city
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    # Complete the tour by returning to the start
    tour.append(start)

    # Compute the total travel cost and the maximum distance between consecutive cities
    total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    return tour, total_cost, max_distance

# Get the BTSP solution
tour, total_cost, max_distance = btsp_heuristic()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")