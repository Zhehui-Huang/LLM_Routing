import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = {
    0: (26, 60),   1: (73, 84),   2: (89, 36),   3: (15, 0),     4: (11, 10),
    5: (69, 22),   6: (28, 11),   7: (70, 2),    8: (47, 50),    9: (60, 29),
    10: (29, 26), 11: (85, 68),  12: (60, 1),   13: (71, 73),   14: (82, 47),
    15: (19, 25), 16: (75, 9),   17: (52, 54),  18: (64, 72),   19: (14, 89)
}

# Heuristic Solution - Nearest Neighbor
def nearest_neighbor_tour(start, cities):
    unvisited = set(cities.keys())
    tour = [start]
    current = start
    unvisited.remove(current)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)
    
    tour.append(start)  # return to the starting city (depot)
    return tour

def calculate_tour_details(tour, cities):
    total_cost = 0
    max_distance = 0
    tour_distances = []
    
    for i in range(len(tour) - 1):
        from_city = tour[i]
        to_city = tour[i + 1]
        distance = euclidean_distance(cities[from_city], cities[to_city])
        tour_distances.append(distance)
        total_cost += distance
        max_distance = max(max_distance, distance)
    
    return tour, total_cost, max_distance

def solve_btsp(cities):
    start_city = 0  # Starting at depot which is city index 0
    tour = nearest_neighbor_tour(start_city, cities)
    tour, total_cost, max_distance = calculate_tour_details(tour, cities)
    return tour, total_cost, max_distance

# Solve the problem
tour, total_cost, max_distance = solve_btsp(cities)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))