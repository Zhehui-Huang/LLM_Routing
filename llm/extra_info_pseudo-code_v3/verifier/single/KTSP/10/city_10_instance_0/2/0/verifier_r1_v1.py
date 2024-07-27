import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_locations):
    # Verify Requirement 1 and 4: The robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 2: Exactly 4 cities are visited, including the depot
    if len(tour) != 5:  # Including depot at start and end
        return "FAIL"
    
    # Verify Requirement 3: Check the travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_locations[tour[i]], city_locations[tour[i+1]])
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City locations given in the problem statement
city_locations = {
    0: (50, 42), # Depot
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Solution provided
tour = [0, 9, 5, 6, 0] 
total_travel_cost = 61.65991894151281

# Conduct the verification
result = verify_solution(tour, total_travel_cost, city_locations)

# Print the result
print(result)