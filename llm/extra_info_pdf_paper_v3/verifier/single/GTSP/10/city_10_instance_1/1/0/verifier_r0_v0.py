import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # Define the cities' coordinates
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
    groups = {
        0: [5, 6, 7],
        1: [2, 3],
        2: [1, 9],
        3: [4, 8]
    }
    
    # Check Requirement 1: Starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Exactly one city from each group
    visited_groups = set()
    for idx in tour[1:-1]:  # Ignore starting and ending city
        for group_id, members in groups.items():
            if idx in members:
                visited_groups.add(group_id)
                break
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Check Requirement 4: Tour output format
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 3 and 5: Travel cost calculation and output total cost
    calculated_cost = 0.0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 5, 2, 9, 8, 0]
total_cost = 183.99

# Verify the solution
result = verify_solution(tour, total_config)
print(result)