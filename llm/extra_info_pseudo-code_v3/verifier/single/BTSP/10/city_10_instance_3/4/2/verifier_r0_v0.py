import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
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
        9: (6, 76)
    }
    
    # Solution details
    tour = [0, 8]
    reported_total_cost = 4.123105625617661
    reported_max_distance = 4.123105625617661
    
    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2
    if len(tour) != len(set(tour)) + 1:  # accounting for the depot city appearing twice
        return "FAIL"
    
    # Requirement 4 (implicitly checked by checking Requirement 1)
    
    # Compute actual tour cost and maximum distance
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        actual_total_cost += dist
        if dist > actual_max_distance:
            actual_max_distance = dist
    
    # Requirement 5
    if not math.isclose(actual_total_cost, reported_total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 6
    if not math.isclose(actual_max_distance, reported_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 3 (Checking if reported_max_distance is minimally possible here would require solving the problem optimally)
    
    return "CORRECT"

# Run the test function
result = test_solution()
print(result)