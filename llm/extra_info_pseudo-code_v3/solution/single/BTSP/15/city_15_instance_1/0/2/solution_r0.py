import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_cost(cities, tour):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

def find_btsp_solution(cities):
    # Calculating all possible edges and sorting them
    num_cities = len(cities)
    edges = []
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean_distance(cities[i], cities[j])
            edges.append((dist, i, j))
    edges.sort()

    for max_edge_length, _, _ in edges:
        possible_tours = permutations(range(1, num_cities))
        for tour in possible_tours:
            tour = [0] + list(tour) + [0]
            total_cost, max_distance = calculate_tour_cost(cities, tour)
            if max_distance <= max_edge_length:
                return tour, total_cost, max_distance

    return [], 0, 0  # return empty if no solution found (should never occur in complete graph)

# Cities are given as: index: (x, y) coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Convert cities to list of coordinates in the right order
city_list = [cities[i] for i in range(len(cities))]

# Solve the BTSP
tour, total_cost, max_distance = find_btsp_solution(city_list)

# Output the result as specified
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")