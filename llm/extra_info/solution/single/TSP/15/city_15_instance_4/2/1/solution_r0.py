import math

# Coordinates of cities including the depot city
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculation of the Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Implementation of the nearest neighbor heuristic for TSP
def nearest_neighbor_tsp(cities):
    start_city = 0
    n = len(cities)
    unvisited = set(range(1, n))
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current_city], cities[city]))
        total_cost += distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    # Return to the depot city
    total_cost += distance(cities[current_city], cities[start_city])
    tour.append(start_city)

    return tour, total_cost

# Solving the TSP for the given cities
tour, total_cost = nearest_neighbor_tsp(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")