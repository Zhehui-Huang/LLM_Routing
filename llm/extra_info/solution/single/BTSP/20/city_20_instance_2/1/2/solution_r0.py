import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates mapping from the given problem
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

def find_tour(cities):
    n = len(cities)
    all_indices = set(cities.keys())
    tour = [0]  # start at the depot
    current_city = 0
    remaining_cities = set(cities.keys()) - {0}
    
    # Constructing a simple greedy tour (not necessarily the best)
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # return to the depot

    # Calculate total travel cost and maximum distance between any two consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    return tour, total_cost, max_distance

# Running the defined function to solve the problem
tour, total_cost, max_distance = find_tour(cities)

# Outputs
print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")