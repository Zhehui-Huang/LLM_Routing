import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_travel_cost, max_distance):
    cities = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69), 5: (47, 39),
        6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
    }
    
    # Check if the robot visits each city exactly once and starts/ends at the depot city 0
    if len(tour) != len(cities) + 1 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"
    
    # Calculate the travel cost and check continuity of the path
    computed_cost = 0
    computed_max_dist = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        if city1 not in cities or city2 not in cities:
            return "FAIL"
        
        distance = euclidean_distance(cities[city1], cities[city2])
        computed_cost += distance
        computed_max_dist = max(computed_max_dist, distance)
    
    # Compare calculated and given travel costs
    if not math.isclose(computed_cost, total_travel_capacity, rel_tol=1e-5):
        return "FAIL"
    
    if not math.isclose(computed_max_dist, max_distance, rel_tol=1e-5):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Provided solution details
solution_details = {'Tour': [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0], 'Total travel cost': 328.3966856465968, 'Maximum distance between consecutive cities': 45.18849411078001}

# Verify the solution
result = verify_solution(solution_details['Tour'], solution_details['Total travel cost'], solution_details['Maximum distance between consecutive cities'])
print(result)