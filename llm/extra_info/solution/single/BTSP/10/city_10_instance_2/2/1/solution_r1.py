import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i, num_cities):
            dist_matrix[i][j] = dist_matrix[j][i] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

def find_tour(cities):
    num_cities = len(cities)
    distances = calculate_distances(cities)
    unvisited = set(range(1, num_cities))
    tour = [0]
    current_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current_city][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(0)  # Return to the depot city

    # Calculate total travel cost and maximum distance between consecutive cities
    total_travel_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = distances[tour[i - 1]][tour[i]]
        total_travel_cost += dist
        if dist > max_distance:
            max_distance = dist

    return tour, total_travel_cost, max_distance

# Coordinates of cities as provided
cities = [
    (90, 3),   # Depot city 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Compute tour, cost and max distance
tour, total_cost, max_consecutive_dist = find_tour(cities)

print("Tour:", tour)
print("Total travel cost: {:.2f}".format(total_cost))
print("Maximum distance between consecutive cities: {:.2f}".format(max_consecutive_dist))