import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, expected_cost):
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76),
    }
    
    # [Requirement 1] Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if all cities are visited exactly once except the depot which should be visited twice
    if sorted(tour) != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        return "FAIL"
    
    # [Requirement 3] Verify the total cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"
    
    # [Requirement 4] is implicitly checked by the outputs
    # This code doesn't specifically validate [Requirement 5] as it's a design choice and cannot be objectively tested in the run
    
    return "CORRECT"

# Provided solution
tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
total_travel_cost = 294.17253892411236

print(verify_solution(tour, total_travel_texcost))