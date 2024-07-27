import math
from collections import Counter

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_tour_cost(tour, city_coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        cost += calculate_euclidean_distance(x1, y1, x2, y2)
    return cost
    
def test_solution(robots_tours, city_coordinates):
    num_cities = len(city_coordinates)
    assert(num_cities == 16), "FAIL: Incorrect number of cities."

    depot = 0
    visited_cities = []
    calculated_overall_cost = 0

    for tour in robots_tours:
        assert(tour[0] == depot and tour[-1] == depot), "FAIL: Tour does not start or end at the depot."
        
        tour_cost = calculate_tour_cost(tour, city_objectiveness)
        calculated_overall_cost += tour_cost

        # Collect visited cities, excluding the depot
        visited_cities.extend(tour[1:-1])

    # Ensure that each non-depot city is visited exactly once
    city_count = Counter(visited_cities)
    for city in range(1, num_cities):
        assert(city_count[city] == 1), f"FAIL: City {city} visited {city_count[city]} times, expected exactly once."

    print("CORRECT")

# Example city coordinates
city_coordinates = [
    (30, 40),  # Depot
    (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69)
]

# Example robot tours
robots_tours = [
    [0, 1, 2, 0],
    [0, 3, 4, 0],
    [0, 5, 6, 0],
    [0, 7, 8, 0],
    [0, 9, 10, 0],
    [0, 11, 12, 0],
    [0, 13, 14, 0],
    [0, 15, 0]
]

# Invoke revised test function without an explicit overall_total_cost
test_solution(robots_tours, city_coordinates)