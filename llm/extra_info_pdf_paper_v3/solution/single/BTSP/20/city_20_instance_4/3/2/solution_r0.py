import math

# Cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Distance calculation (Euclidean)
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calculate distances between all pairs of cities
dist_matrix = {}
for i in cities:
    for j in cities:
        dist_matrix[(i, j)] = distance(i, j)

# Using a simple heuristic - Nearest Neighbor algorithm modified to minimize max distance in path
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    tour = [start_city]
    current_city = start_city
    unvisited.remove(start_city)
    total_cost = 0
    max_leg_distance = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[(current_city, city)])
        next_distance = dist_matrix[(current_city, next_city)]
        tour.append(next_city)
        total_cost += next_distance
        max_leg_distance = max(max_leg_distance, next_distance)
        current_city = next_city
        unvisited.remove(next_city)

    # Return to start city
    return_to_start_distance = dist_matrix[(tour[-1], start_city)]
    tour.append(start_city)
    total_cost += return_to_start_distance
    max_leg_distance = max(max_leg_distance, return_to_start_distance)

    return tour, total_cost, max_leg_distance

# Compute the tour from depot
tour_result = nearest_neighbor_tour(0)

# Formatted output
print("Tour:", tour_result[0])
print("Total travel cost:", round(tour_result[1], 2))
print("Maximum distance between consecutive cities:", round(tour_result[2], 2))