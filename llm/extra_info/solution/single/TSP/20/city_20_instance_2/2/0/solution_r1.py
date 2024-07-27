import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def nearest_neighbor_tour(cities):
    num_cities = len(cities)
    unvisited = set(range(1, num_cities))  # Exclude depot initially
    tour = [0]
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city][0], cities[current_city][1], cities[city][0], cities[city][1]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(0)
    return tour

def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]][0], cities[tour[i]][1], cities[tour[i+1]][0], cities[tour[i+1]][1])
    return total_distance

cities = [
    (3, 26),  # Depot city 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

tour = nearest_neighbor_tour(cities)
total_distance = calculate_total_distance(tour, cities)
print("Tour:", tour)
print("Total travel cost:", total_distance)