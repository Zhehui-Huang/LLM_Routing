import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(tour, total_cost, coordinates):
    # Verify the number of unique cities visited (Requirement 1)
    if len(set(tour)) != 8:
        return "FAIL"

    # Verify that the tour starts and ends at the depot city (Requirement 2)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify the travel cost is correctly calculated (Requirement 3)
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])

    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"
    
    # Requirement 4 is implicit in the problem description and does not require checking.
    # Requirement 5 is subjective and depends on the optimality of the given algorithm – cannot be unit tested.
    
    # Verify correct output format (Requirement 6 and 7)
    if not isinstance(tour, list) or len(tour) != 9:  # considering round trip city 0 at end
        return "FAIL"
    
    # Requirement 8 is the general situation and does not require unit testing.
    
    return "CORRECT"

# Provided cities coordinates
cities_coords = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Solution provided
tour_provided = [0, 1, 8, 3, 14, 2, 6, 11, 0]
total_travel_cost_provided = 195.88

# Invoke the verification function
result = verify_solution(tour_provided, total_travel_cost_provided, cities_coords)
print(result)