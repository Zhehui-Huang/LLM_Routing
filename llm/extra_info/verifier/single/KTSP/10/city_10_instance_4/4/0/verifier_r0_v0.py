import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_solution():
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    tour = [0, 1, 3, 4, 5, 7, 8, 9, 0]
    reported_cost = 363.60
    
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Exactly 8 cities visited including depot
    if len(set(tour)) != 9:  # including depot both in start and end
        return "FAIL"
    
    # Calculate travel cost to check Requirement 3 and 5
    computed_cost = 0
    for i in range(len(tour)-1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    computed_cost = round(computed_with_accurate_rounding, 2)  # To match the given precision

    # Requirement 5: Output the total travel cost of the tour
    if not math.isclose(computed_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Running the test
print(test_solution())