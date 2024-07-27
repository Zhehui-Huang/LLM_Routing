import math

# City coordinates
cities = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

# Initial tour using nearest neighbor heuristic starting from the depot
def nearest_neighbor_tour(start, cities):
    unvisited = set(range(1, len(cities)))
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # return to start
    return tour

# Calculate total tour cost
def tour_cost(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Initial tour
tour = nearest_neighbor_tour(0, cities)
cost = tour_cost(tour, cities)

# Output results
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))