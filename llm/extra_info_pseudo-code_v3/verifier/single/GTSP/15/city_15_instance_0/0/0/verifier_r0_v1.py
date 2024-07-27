import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_cost):
    city_coordinates = {
        0: (9, 93),
        1: (8, 51),
        2: (74, 99),
        3: (78, 50),
        4: (21, 23),
        5: (88, 59),
        6: (79, 77),
        7: (63, 23),
        8: (19, 76),
        9: (21, 38),
        10: (19, 65),
        11: (11, 40),
        12: (3, 21),
        13: (60, 55),
        14: (4, 39)
    }
    
    city_groups = [
        [2, 7, 10, 11, 14],
        [1, 3, 5, 8, 13],
        [4, 6, 9, 12]
    ]
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # Exclude the depot at start and end
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups[i] += 1

    if any(count != 1 for count in visited_groups):
        return "FAIL"
    
    # Calculate the total distance and compare with the provided total cost
    calculated_cost = 0.0
    n = len(tour)
    for i in range(n - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    # Check against the given tolerance for possible float precision errors
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution to verify
tour = [0, 10, 1, 9, 0]
total_cost = 122.22

# Unit test
print(test_solution(tour, total_cost))