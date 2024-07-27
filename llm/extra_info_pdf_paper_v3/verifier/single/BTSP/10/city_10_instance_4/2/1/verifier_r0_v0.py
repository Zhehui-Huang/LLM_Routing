import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def total_travel_cost(tour, cities):
    return sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def max_distance_between_cities(tour, cities):
    return max(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def testcase():
    cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
    tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
    expected_total_cost = 408.41
    expected_max_distance = 61.68
    
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    if sorted(tour[:-1]) != list(range(len(cities))):
        return "FAIL"
    
    # Calculate the actual total cost and maximum distance
    total_cost = total_travel_cost(tour, cities)
    max_distance = max_distance_between_cities(tour, cities)
    
    # Compare with expected results allowing for small numerical precision issues
    if not (math.isclose(total_cost, expected_total_cost, rel_tol=1e-2) and
            math.isclose(max_distance, expected_max_distance, rel_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Run the test case
print(testcase())