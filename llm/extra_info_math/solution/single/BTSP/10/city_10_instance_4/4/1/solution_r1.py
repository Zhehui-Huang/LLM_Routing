import math
from sys import maxsize

# Coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Dictionary to store distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Nearest neighbor algorithm to find a route
def nearest_neighbor(start=0):
    unvisited = set(cities.keys())
    tour = [start]
    unvisited.remove(start)
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[(current, city)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    # Completing the tour by returning to the start
    tour.append(start)
    return tour

# Calculate information about the tour
def tour_info(tour):
    total_distance = 0
    max_distance = 0
    n = len(tour)
    
    for i in range(n - 1):
        d = distances[(tour[i], tour[i + 1])]
        total_distance += d
        if d > max_distance:
            max_distance = d
    
    return total_distance, max_distance

# Get the tour and calculate necessary details
tour = nearest_neighbor()
total_distance, max_distance = tour_info(tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")