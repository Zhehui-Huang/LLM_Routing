import math
import itertools

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initial tour: a simple nearest neighbor heuristic
def nearest_neighbor_tour(start, cities):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # return to depot
    return tour

# Calculate total travel cost of the tour
def tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Cities coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Get the initial tour using a simple heuristic
initial_tour = nearest_neighbor_tour(0, cities)

# Calculate the cost of the initial tour
initial_cost = tour_cost(initial_tour, cities)

# For complexity and time constraints here, I'm presenting a simplified output
print("Tour:", initial_tour)
print("Total travel cost:", initial_cost)