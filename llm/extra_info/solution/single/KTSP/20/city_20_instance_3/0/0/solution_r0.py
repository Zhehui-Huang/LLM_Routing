import math

# Coordinates of cities: city index maps to its (x, y) coordinates
coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def find_tour(start_city, num_cities):
    visited = {start_city}
    tour = [start_city]
    current_city = start_city

    while len(tour) < num_cities:
        next_city = None
        min_distance = float('inf')
        for city in coordinates:
            if city not in visited:
                distance = euclidean::::::::::::::::::::::::::::::::::::::::::::::::::distance(current_city, city)
                if distance < min_distance:
                    min_distance = distance
                    next_city = city
        visited.add(next_city)
        tour.append(next_city)
        current_city = next_city

    tour.append(start_city)  # return to depot

    return tour

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

num_cities_including_depot = 13
tour = find_tour(0, num_cities_including_depot)
total_travel_cost = calculate_total_distance(tour)

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)