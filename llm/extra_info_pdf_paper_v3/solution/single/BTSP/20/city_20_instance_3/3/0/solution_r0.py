import math

# City coordinates
coordinates = [
    (30, 56),  # Depot city 0
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72)   # City 19
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute the distance matrix
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def nearest_neighbor_modified():
    unvisited = set(range(1, n))
    tour = [0]
    max_distance_between_cities = 0
    total_travel_cost = 0

    current_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        next_distance = distance_matrix[current_city][next_city]
        max_distance_between_cities = max(max_distance_between_cities, next_distance)
        total_travel_cost += next_distance
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    # Closing the tour back to the depot city
    final_leg_distance = distance_matrix[current_city][0]
    total_travel_cost += final_leg_distance
    tour.append(0)
    max_distance_between_cities = max(max_distance_between_cities, final_leg_distance)

    return tour, total_travel_cost, max_distance_between_cities

# Get the results from the nearest_neighbor_modified function
result_tour, result_total_cost, result_max_distance = nearest_neighbor_modified()

# Output result
print("Tour:", result_tour)
print("Total travel cost:", result_total_cost)
print("Maximum distance between consecutive cities:", result_max_distance)