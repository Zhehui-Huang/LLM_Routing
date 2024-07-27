import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def check_solution(tour, expected_cost):
    # City coordinates (indexed from 0 to 9)
    coordinates = {
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
    
    # Requirement 1: starts and ends at depot 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 5 cities including the depot
    if len(set(tour)) != 5 or len(tour) != 6:
        return "FAIL"
    
    # Requirement 3 & 4: Calculate total travel cost and check the route
    total_distance = 0
    for i in range(len(tour) - 1):
        if tour[i] not in coordinates or tour[i+1] not in coordinates:
            return "FAIL"
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Requirement 5: Correct formatting and calculation of travel cost
    if abs(expected_cost - round(total_distance, 2)) > 0.01:  # Allowing small floating-point variance
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
# Tour: [0, 2, 9, 7, 6, 0]
# Total travel cost: 195.84
tour_provided = [0, 2, 9, 7, 6, 0]
total_cost_provided = 195.84

# Run the test
test_result = check_solution(tour_provided, total_cost_provided)
print(test_result)