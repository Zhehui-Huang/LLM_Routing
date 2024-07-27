import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_ktsp_solution(tour, reported_cost):
    # Cities coordinates indexed by city number
    cities = {
        0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59), 
        6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 
        12: (3, 21), 13: (60, 55), 14: (4, 39)
    }
    
    # Requirements checks
    if len(tour) != 5:  # includes starting and ending at depot
        return "FAIL"
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(set(tour)) != 5:  # Excluding repeats, should be exactly 5 unique cities (including depot)
        return "FAIL"
    
    # Calculate total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Compare calculated to reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-2):  # Allowing small tolerance
        return "FAIL"

    return "CORRECT"

# The provided example solution
example_tour = [0, 1, 10, 8, 0]
example_reported_cost = 90.54

# Running the test function
result = test_ktsp_solution(example_tour, example_reported_cost)
print(result)