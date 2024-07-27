import math

def calculate_distance(city1, city2):
    return round(math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2), 2)

def verify_solution(tours, city_coordinates):
    # Requirement 1 has already been met since coordinates input is fixed
    visited_cities = set()
    total_calculated_cost = 0.0

    robot_start_depot = 0  # All robots start from depot city 0 as indicated in the tours
    expected_tour_total_cost = 377.42

    for robot_id, tour in enumerate(tours):
        tour_cost = 0
        previous_city_index = tour[0]
        
        for city_index in tour[1:]:
            tour_cost += calculate_distance(city_coordinates[previous_city_index], city_coordinates[city_index])
            previous_city_index = city_index
        
        # Add return to start if needed
        if tour[-1] != robot_start_depot:
            tour_cost += calculate_distance(city_coordinates[tour[-1]], city_coordinates[robot_start_depot])
        
        total_calculated_cost += tour_cost
        visited_cities.update(tour)
        
        # Requirement 6 met if costs are within reasonable float comparison tolerance
        if not math.isclose(tour_cost, tour_costs[robot_id], abs_tol=0.01):
            return "FAIL"

    # Requirement 3: Check for unique city visits
    if len(visited_cities) != 23:
        return "FAIL"

    # Requirement 7: Check if the sum of tour costs matches expected overall cost
    if not math.isclose(total_calculated_cost, expected_tour_total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Defined city coordinates from problem statement
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Tours and costs as provided
tours = [
    [0, 21, 7, 9], [0, 16, 5, 17], [0, 22, 6, 8], [0, 1, 12, 15], [0, 14, 20, 18],
    [0, 3, 10, 19], [0, 2, 13], [0, 4, 11]
]
tour_costs = [32.39, 38.10, 63.40, 36.37, 78.89, 68.95, 30.08, 29.23]

# Verify tours based on constraints
result = verify_solution(tours, cities)
print(result)