import math

# Given city coordinates
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

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def nearest_neighbor_tour(start_city):
    current_city = start_city
    tour = [current_city]
    unvisited_cities = set(cities.keys()) - {current_city}
    total_distance = 0.0

    while unvisited_cities:
        nearest_city, min_distance = min(
            ((city, euclidean_distance(cities[current_city], cities[city])) for city in unvisited_cities),
            key=lambda x: x[1]
        )
        tour.append(nearest_city)
        total_distance += min_distance
        current_city = nearest_city
        unvisited_cities.remove(current_city)

    # Return to the start city (depot)
    return_to_depot_distance = euclidean_distance(cities[current_city], cities[start_city])
    total_distance += return_to_depot_distance
    tour.append(start_city)
    return tour, total_distance

# Finding the tour and cost
tour, total_cost = nearest_neighbor_tour(0)

# Output the result in the required format
print("Tour:", tour)
print("Total travel cost:", round(total_cost))