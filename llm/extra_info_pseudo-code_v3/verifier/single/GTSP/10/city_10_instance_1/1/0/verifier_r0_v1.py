import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution(tour, total_travel_cost):
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    city_groups = {
        0: [5, 6, 7],
        1: [2, 3],
        2: [1, 9],
        3: [4, 8]
    }
    
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited = set(tour[1:-1])  # exclude the starting and ending 0
    if any(sum(1 for city in group if city in visited) != 1 for group in city_groups.values()):
        return "FAIL"
    
    # Requirement 4: Tour representation
    if not all(city in cities for city in tour):
        return "FAIL"
    
    # Requirement 3: Correct calculation of travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Requirement 5: Correct total travel cost
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Example test case
tour = [0, 5, 2, 9, 8, 0]
total_travel_cost = 183.98559431675523
result = test_solution(tour, total_travel_cost)
print(result)  # Output should be "CORRECT" if all requirements are met