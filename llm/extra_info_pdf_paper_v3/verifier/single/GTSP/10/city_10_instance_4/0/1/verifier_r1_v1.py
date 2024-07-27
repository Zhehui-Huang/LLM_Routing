import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost):
    # Coordinates for each city index
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
    
    # City groups
    groups = [
        [1, 4],
        [2, 6],
        [7],
        [5],
        [9],
        [8],
        [3]
    ]
    
    # Checking Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Checking Requirement 2: One city from each group
    visited_groups = [0] * len(groups)
    for city_idx in tour[1:-1]:  # excluding the depot city at start and end
        found_in_group = False
        for i, group in enumerate(groups):
            if city_idx in group:
                visited_groups[i] += 1
                found_in_group = True
        if not found_in_group:
            return "FAIL"
    if any(count != 1 for count in visited_groups):
        return "FAIL"
    
    # Checking Requirement 3: Total of 8 cities, including start and end
    if len(tour) != 9:
        return "FAIL"
    
    # Calculate and verify total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(*cities[city1], *cities[city2])
    
    # Checking Requirement 4: Travel cost matches
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Provided tour and cost
tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
total_travel_cost = 371.1934423276749

# Validate and check if the solution is correct
print(verify_solution(tour, total_travel_cost))