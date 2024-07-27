import math

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(tour, total_travel_cost):
    # Coordinates for each city
    coordinates = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
        4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
        8: (61, 90), 9: (42, 49)
    }
    
    # Verification Criteria
    # Criteria 1: Check if there are 10 cities including the depot.
    if len(coordinates) != 10:
        return "FAIL"
    
    # Criteria 2: Check if the tour starts and ends at the depot.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Criteria 3: Check if exactly 4 cities are visited including the depot.
    if len(tour) != 5:
        return "FAIL"
    
    # Criteria 4: Calculate the travel cost and compare it to the provided cost.
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    if not math.isclose(computed_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Criteria 5: Ensure the format is a list of indices followed by total cost.
    # This is implicitly covered by the input format provided and the computed return.
    
    return "CORRECT"

# Given solution
tour_provided = [0, 9, 5, 6, 0]
total_cost_provided = 61.66

# Test the solution
result = verify_solution(tour_provided, total_cost_provided)
print(result)