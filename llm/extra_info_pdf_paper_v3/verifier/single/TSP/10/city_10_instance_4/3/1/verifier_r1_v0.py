import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tsp_solution():
    # Given cities coordinates including the depot
    cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
    
    # Given solution
    tour = [0, 3, 1, 6, 7, 5, 9, 8, 2, 4, 0]
    reported_total_cost = 425.5547541188898
    
    # Test conditions
    # 1. Tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # 2. Each city must be visited exactly once, except the depot
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
    
    # 3. Calculate the total travel cost and compare
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    
    if not math.isclose(calculated_cost, reported_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # 4. All cities are distinct and labeled correctly
    if len(set(tour)) != len(tour):
        return "FAIL"
    
    # Since all checks have passed
    return "CORRECT"

# Execute the test function and print the result
print(test_tsp_solution())