def euclidean_distance(city1, city2):
    from math import sqrt
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_tour_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return total_cost

def verify_solution(robot_tours, city_coordinates):
    visited_cities = set()
    all_city_indices = set(range(1, len(city_coordinates)))  # Excludes depot(0) as a destination

    # Requirement 1: All cities visited exactly once and by one robot only
    for tour in robot_tours:
        for city in tour:
            if city != 0:
                if city in visited_cities:
                    return "FAIL"
                visited_cities.add(city)

    if visited_cities != all_city_indices:
        return "FAIL"

    # Requirement 2: Each robot starts and ends at the depot
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Requirement 3: Already minimized in the problem solution; calculate to compare with the expected maximum travel
    max_travel_cost_computed = max([calculate_tour_cost(tour, city_coordinates) for tour in robot_tours])

    expected_max_travel_cost = 122.64  # As provided in the problem solution
    if abs(max_travel_cost_computed - expected_max_travel_cost) > 0.1:
        return "FAIL"

    # Passed all checks
    return "CORRECT"

city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

tours = [
    [0, 20, 17, 19, 0], [0, 16, 1, 9, 0], [0, 4, 11, 3, 0],
    [0, 15, 18, 14, 0], [0, 2, 13, 12, 0], [0, 6, 10, 8, 0],
    [0, 7, 22, 0], [0, 21, 5, 0]
]

result = verify_solution(tours, city_coords)
print(result)