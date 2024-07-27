import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour_requirements(tour, total_cost, cities):
    # Constants
    depot_city = 0

    # [Requirement 1] Each city, except for the depot city, must be visited exactly once by the robot.
    cities_visited = tour[1:-1]  # Exclude the starting and ending depot city
    if sorted(cities_visited) != list(range(1, len(cities))):
        return "FAIL"

    # [Requirement 2] The robot must start and end the tour at the depot city.
    if tour[0] != depot_city or tour[-1] != depot_city:
        return "FAIL"

    # [Requirement 3 & 4] Calculate total cost of the given tour and compare with provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Use a small tolerance for floating-point comparisons
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
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