import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, city_coordinates, groups):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = [0] * len(groups)
    for city in tour:
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
    if any(count != 1 for count in visited_groups):
        return "FAIL"

    # Calculate the total travel cost and compare
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    # Due to floating point precision, use a small epsilon for comparison
    if abs(calculated_cost - total_cost) > 0.1:
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 1, 5, 7, 9, 8, 2, 3, 0]
total_travel_cost = 279.02

# Given city coordinates and groups
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Check the solution
result = verify_solution(tour, total_travel_cost, cities, groups)
print(result)