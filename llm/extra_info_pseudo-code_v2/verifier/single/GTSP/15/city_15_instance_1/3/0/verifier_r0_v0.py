import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # City coordinates
    city_coordinates = {
        0: (29, 51),
        1: (49, 20),
        2: (79, 69),
        3: (17, 20),
        4: (18, 61),
        5: (40, 57),
        6: (57, 30),
        7: (36, 12),
        8: (93, 43),
        9: (17, 36),
        10: (4, 60),
        11: (78, 82),
        12: (83, 96),
        13: (60, 50),
        14: (98, 1)
    }
    
    # Groups
    city_groups = [
        [1, 2, 5, 6],
        [8, 9, 10, 13],
        [3, 4, 7],
        [11, 12, 14]
    ]
    
    # Check the cities in the tour
    if len(tour) != 6:
        return "FAIL"
    
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check one city from each group
    selected_groups = set()
    for city in tour[1:-1]:
        for i, group in enumerate(city_groups):
            if city in group:
                selected_groups.add(i)
                
    if len(selected_groups) != len(city_groups):
        return "FAIL"
    
    # Calculate and check travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-02):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and total cost
tour = [0, 5, 10, 4, 11, 0]
total_cost = 184.24

# Verify the solution
result = verify_solution(tour, total_cost)
print(result)