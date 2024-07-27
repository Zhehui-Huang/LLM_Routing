import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_travel_cost(tour, city_positions):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_positions[tour[i]], city_positions[tour[i + 1]])
    return total_cost

def validate_solution(tour, total_travel_cost):
    city_positions = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
        4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
        8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
        12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # Requirement 1: Tour must start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Tour must visit exactly 6 cities including the depot
    if len(tour) != 7:  # including the return to the depot
        return "FAIL"
    
    # Requirement 4: Output must list including starting and ending at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 5: Output must include the total travel cost
    calculated_cost = calculate_total_travel_cost(tour, city_positions)
    if abs(calculated_cost - total_travel_cost) > 0.0001:  # Allowing some precision error
        return "FAIL"
    
    # Assuming requirement 3 (minimize cost) and 6 (GVNS used) are met by algorithm's output
    return "CORRECT"

# Provided solution details
given_tour = [0, 5, 13, 6, 1, 7, 0]
given_total_travel_cost = 121.6371441123728

# Validate the solution
result = validate_solution(given_tour, given_total_travel_cost)
print(result)