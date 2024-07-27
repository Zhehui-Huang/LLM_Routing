def check_tour_requirements(tour, total_cost, cities):
    # Constants
    depot_city = 0
    
    # Convert city tuples to complex to use in distance calculation
    city_complex = [complex(*city) for city in cities]

    # [Requirement 1] Each city, except for the depot city, must be visited exactly once by the robot.
    cities_visited = tour[1:-1]  # Remove the depot city occurrences except the start and end
    if set(cities_visited) != set(range(1, len(cities))):
        return "FAIL"

    # [Requirement 2] The robot must start and end the tour at the depot city.
    if tour[0] != depot_city or tour[-1] != depot_city:
        return "FAIL"

    # [Requirement 3 & 4] Using the given distances, verify total cost by recalculating from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        calculated_cost += abs(city_complex[city_from] - city_complex[city_to])

    # Floating-point arithmetic can introduce tiny differences
    if not (abs(calculated with tolerance due to potential floating point precision issues.
    if not abs(calculated_cost - total_cost) < 1e-6:
        return "FAIL"

    # If all checks are passed, return "CORRECT"
    return "CORRECT"

# Provided solution and city coordinates
tour_solution = [0, 14, 5, 9, 10, 13, 6, 8, 11, 2, 7, 3, 12, 4, 1, 0]
total_travel_cost_solution = 303.3094531921134
cities_coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Call the verification function
result = check_tour_requirements(tour_solution, total_travel_cost_solution, cities_coordinates)
print(result)