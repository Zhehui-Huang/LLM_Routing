import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, total_travel_cost):
    # City coordinates
    cities = {
        0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
        5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
    }
    
    # Requirement 1: Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Requirement 2: Check if exactly 6 cities (including depot) are visited
    if len(tour) != 7:  # including the return to the depot
        return False

    # Requirement 3: Calculate and compare the total travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(computed_cost, total_travel_cost, rel_tol=1e-9):
        return False
    
    # If all checks passed
    return True

# Provided solution details
tour = [0, 8, 5, 2, 1, 9, 0]
total_travel_cost = 183.85354044487238

# Validation
if validate_solution(tour, total_travel_cost):
    print("CORRECT")
else:
    print("FAIL")