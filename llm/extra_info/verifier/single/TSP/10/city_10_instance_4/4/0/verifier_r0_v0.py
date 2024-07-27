import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost):
    # List of cities with their coordinates
    cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
    
    # Check the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities are visited exactly once except the depot
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "1FAIL"
    
    # Calculate total travel cost using Euclidean distances
    calculated_cost = 0
    for i in range(len(tour)-1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(city1[0], city1[1], city2[0], city2[1])
    
    # Check if the total travel cost matches
    if not math.isclose(calculated_cost, total_travel_stated_cost, abs_tol=1e-6):
        return "2FAIL"
    
    # If all checks pass, the solution is likely correct
    return "CORRECT"

# Provided tour and cost
tour = [0, 4, 7, 5, 1, 9, 8, 2, 6, 3, 0]
total_travel_stated_cost = 321

# Verify and print result
result = verify_solution(tour, total_travel_stated_cost)
print(result)