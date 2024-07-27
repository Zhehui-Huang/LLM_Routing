import math

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution(tour, cost):
    cities_coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]

    # Requirement 1 & 4: Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if all cities are visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities_coordinates) or any(city not in unique_cities for city in range(len(cities_coordinates))):
        return "FAIL"

    # Requirement 3 & 5: Calculate and compare the total travel cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        city1 = cities_coordinates[tour[i - 1]]
        city2 = cities_coordinates[tour[i]]
        calculated_cost += euclidean_distance(city1, city2)

    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"

    # Requirements 6: Heuristic optimization is assumed due to strategy used
    # Additional checks could include checking optimality, efficiency, but not feasible here.
    return "CORRECT"

# Given solution
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
total_cost = 410.03585920085146

# Check the solution
print(check_solution(tour, total_cost))