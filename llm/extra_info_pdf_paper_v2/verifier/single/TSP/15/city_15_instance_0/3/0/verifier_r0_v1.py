import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, city_coordinates):
    # [Requirement 1] Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once
    all_cities = set(range(len(city_coordinates)))
    visited_cities = set(tour)
    if visited_cities != all_cities:
        return "FAIL"
    
    # [Requirement 3 & 5] Check if the travel cost matches the calculated total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # [Requirement 4] Check the format of the tour
    if not isinstance(tour, list) or not all(isinstance(x, int) for x in tour):
        return "FAIL"
    
    return "CORRECT"

# City coordinates based on provided environment info
city_coordinates = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
                    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Solution provided
tour_solution = [0, 8, 10, 1, 11, 14, 12, 4, 9, 7, 3, 5, 6, 2, 13, 0]
total_travel_cost_solution = 359.54

# Verifying the solution
verification_result = verify_solution(tour_solution, total_travel_cost_solution, city_coordinates)

print(verificationn_result)