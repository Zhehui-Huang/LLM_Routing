import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution():
    cities = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }

    tour = [0, 8, 5, 2, 1, 9, 0]
    claimed_total_cost = 183.85

    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly 6 cities including the depot
    if len(set(tour)) != 6:
        return "FAIL"

    # Requirement 3 & 5: Correct tour distance calculation
    actual_total_cost = sum(calculate_euclidean_distance(cities[tour[i]][0], cities[tour[i]][1],
                                                         cities[tour[i+1]][0], cities[tour[i+1]][1])
                            for i in range(len(tour)-1))
    
    # Checking the precision up to 2 decimal places
    if round(actual_total_cost, 2) != round(claimed_total_cost, 2):
        return "FAIL"
    
    # Output CORRECT if all checks passed
    return "CORRECT"
    
# Execute the test function
result = test_number_of_cities_visited()
print(result)