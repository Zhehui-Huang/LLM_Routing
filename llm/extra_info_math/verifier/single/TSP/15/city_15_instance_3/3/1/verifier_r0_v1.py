import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates):
    # Requirement 1: Start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit each city exactly once, except the depot city
    visited_cities = tour[1:-1]  # exclude the repeated depot city at the end
    if len(set(visited_cities)) != len(city_coordinates) - 1:
        return "FAIL"

    # Requirement 3 and Requirement 4: Calculate the travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])

    # Requirement 6: Check the total travel cost
    if abs(calculated_cost - total_travel_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Cities Coordinates including the depot
city_coordinates = [
    (16, 90),  # City 0: Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Solution provided
tour = [0, 6, 8, 13, 14, 5, 9, 10, 7, 3, 12, 4, 1, 0]
total_travel_cost = 276.4882198966477

# Verifying the solution
result = verify_solution(tour, total_travel_cost, city_coordinates)
print(result)