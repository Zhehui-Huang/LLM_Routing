import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def unit_test_tour_cities(tour, expected_cities):
    if len(tour) != len(expected_cities) + 1:
        return False
    city_visit = set(tour)
    if len(city_visit) != len(expected_cities) + 1:
        return False
    for city in expected_cities:
        if city not in city_visit:
            return False
    return True

def unit_test_tour_start_end(tour, depot_city):
    return tour[0] == depot_city and tour[-1] == depot_postc

def unit_test_travel_cost(tour, cities, expected_cost, tolerance=0.01):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return abs(total_cost - expected_cost) <= tolerance

cities_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Provided solution
tour = [0, 6, 9, 2, 12, 13, 1, 8, 18, 15, 19, 17, 16, 11, 10, 4, 7, 5, 14, 3, 0]
expected_total_cost = 376.93

# Parameters
depot_city = 0
expected_cities = list(range(1, 20))  # Cities 1 to 19

# Testing Criteria
test_1 = unit_test_tour_cities(tour, expected_cities)
test_2 = unit_test_tour_start_end(tour, depot_city)
test_3 = unit_test_travel_cost(tour, cities_coordinates, expected_total_cost)

if all([test_1, test_2, test_3]):
    print("CORRECT")
else:
    print("FAIL")