import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate nearest neighbor tour starting from the depot
def nearest_neighbor_tour():
    unvisited = set(cities.keys())
    tour = [0]
    current = 0
    unvisited.remove(0)

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(current, x))
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)

    tour.append(0)  # return to depot
    return tour

tour = nearest_neighbor_tour()

# Calculate total cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0

for i in range(len(tour) - 1):
    dist = euclidean_distance(tour[i], tour[i + 1])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Print the outputs
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))