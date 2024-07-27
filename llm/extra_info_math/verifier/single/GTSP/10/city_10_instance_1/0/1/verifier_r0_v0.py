import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost):
    # City coordinates from the problem statement
    city_coords = {
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
    
    # City groups defining the constraints
    city_groups = [
        [5, 6, 7],
        [2, 3],
        [1, 9],
        [4, 8]
    ]
    
    # [Requirement 1] Check one city from each group is visited
    cities_visited = set(tour)
    for group in city_groups:
        if not set(group).intersection(cities_visited):
            return "FAIL"

    # [Requirement 2] Check start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 3] Check the travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Solution and provided total travel cost
tour = [0]
total_travel_cost = 0

# Verify the solution
solution_status = verify_solution(tour, total_travel_cost)
print(solution_status)