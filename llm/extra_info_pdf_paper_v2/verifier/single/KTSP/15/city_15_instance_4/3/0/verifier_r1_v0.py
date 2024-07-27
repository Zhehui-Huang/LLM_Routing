import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_total_cities_visited(tour):
    return len(tour) == 13  # Includes starting and ending at the depot city

def test_start_and_end_depot_city(tour):
    return tour[0] == 0 and tour[-1] == 0

def test_unique_cities(tour):
    return len(set(tour)) == 13

def test_total_travel_cost(tour, cities, expected_cost):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return round(total_cost, 2) == round(expected_cost, 2)

# City coordinates: (index_0_based: (x, y))
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Tour and cost provided
provided_tour = [0, 1, 10, 8, 14, 3, 6, 12, 4, 7, 9, 0]
provided_cost = 241.29

# Perform the checks
if (test_total_cities_visited(provided_tour) and
    test_start_and_end_depot -city(provided_tour) and
    test_unique_cities(provided_tour) and
   test_total_travel_cost(provided_tour, cities, provided_cost)):
    print("CORRECT")
else:
    print("FAIL")