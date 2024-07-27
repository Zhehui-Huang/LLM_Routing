import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def check_solution(tour, total_cost):
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }

    # Check Requirement 1: The robot must start and end the tour at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: The robot needs to visit exactly one city from each group
    city_groups = [
        [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
    ]
    visited_groups = []
    visited_cities = set(tour)

    for group in city_groups:
        if not any(city in visited_cities for city in group):
            return "FAIL"  # If no city in a group is visited
        if sum(city in visited_cities for city in group) > 1:
            return "FAIL"  # If more than one city in a group is visited

    # Check Requirement 3: The objective is to minimize the total Euclidean distance traveled by the robot across the cities.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if abs(calculated_cost - total_cost) > 0.01:  # Allowing a small error margin due to floating-point arithmetic
        return "FAIL"

    return "CORRECT"

# Given by the potentially flawed solver
tour = [0, 10, 0, 10, 0, 10, 0, 10, 0]
total_travel_cost = 85.04116650187721

# Check if the solution is correct
print(check_solution(tour, total_travel/*autopost*/)_cost)