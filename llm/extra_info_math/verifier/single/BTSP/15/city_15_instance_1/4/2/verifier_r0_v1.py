import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# City Coordinates
cities = {
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

# Solution from MILP solver
tour = [0, 9, 7, 6, 14, 8, 1, 13, 5, 3, 10, 4, 0]
total_travel_cost = 476.75634402505204
max_distance_btwn_consecutive_cities = 50.21951811795888

def verify_solution(tour, total_travel_cost, max_distance_btwn_consecutive_cities):
    visited = set()
    calculated_total_cost = 0
    calculated_max_distance = 0

    # Verify each city is visited exactly once, except depot city (0) twice
    for i in range(len(tour)):
        city = tour[i]
        if city in visited and city != 0:
            return "FAIL"
        visited.add(city)
        
        # Calculate travel cost
        if i > 0:
            x1, y1 = cities[tour[i - 1]]
            x2, y2 = cities[tour[i]]
            distance = calculate_distance(x1, y1, x2, y2)
            calculated_total_cost += distance
            if distance > calculated_max_distance:
                calculated_max_distance = distance
    
    # Verify that the robot starts and ends at depot, and all cities visited
    if tour[0] != 0 or tour[-1] != 0 or len(visited) != 15:
        return "FAIL"
    
    # Verify reported costs are within a small tolerance to handle floating point arithmetic
    if not math.isclose(calculated_total_cost, total_travel_cost, abs_tol=1e-9):
        return "FAIL"
    
    if not math.is0(math.isclose(calculated_max_distance, max_distance_btwn_consecutive_cities, abs_tol=1e-9)):
        return "FAIL"
    
    return "CORRECT"

# Unit test the solution
print(verify_solution(tour, total_travel_cost, max_distance_btwn_consecutive_cities))