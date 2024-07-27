import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def test_solution(tour, total_cost):
    city_coordinates = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }
    
    city_groups = [
        [8, 12, 14],
        [7, 10, 11],
        [4, 6, 9],
        [1, 3, 13],
        [2, 5]
    ]
    
    # Check starting and ending at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups[i] += 1
                break
    
    if any(count != 1 for count in visited_groups):
        return "FAIL"
    
    # Check Euclidean distance calculation and total is correct
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        calculated_total_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution to test
tour = [0, 12, 10, 4, 3, 2, 0]
total_cost = 138.15

# Run the test
result = test_solution(tour, total_cost)
print(result)