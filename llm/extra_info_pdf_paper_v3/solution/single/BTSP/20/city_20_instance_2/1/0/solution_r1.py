import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_all_distances(cities):
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

def find_tour(cities):
    num_cities = len(cities)
    distances = calculate_all_distances(cities)
    unvisited = set(range(1, num_cities))
    tour = [0]  # Start at the depot
    current_city = 0
    max_distance = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        new_dist = distances[current_city][next_city]
        max_distance = max(max_distance, new_dist)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    tour.append(0)
    max_distance = max(max_distance, distances[current_city][0])
    total_travel_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

    return tour, total_travel_cost, max_distance

cities = [
    (3, 26),   # Depot
    (85, 72),  # 1
    (67, 0),   # 2
    (50, 99),  # 3
    (61, 89),  # 4
    (91, 56),  # 5
    (2, 65),   # 6
    (38, 68),  # 7
    (3, 92),   # 8
    (59, 8),   # 9
    (30, 88),  # 10
    (30, 53),  # 11
    (11, 14),  # 12
    (52, 49),  # 13
    (18, 49),  # 14
    (64, 41),  # 15
    (28, 49),  # 16
    (91, 94),  # 17
    (51, 58),  # 18
    (30, 48)   # 19
]

tour, total_cost, max_distance = find_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)