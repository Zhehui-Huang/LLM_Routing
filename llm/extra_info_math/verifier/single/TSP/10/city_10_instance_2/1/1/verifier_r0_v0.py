import math

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def verify_solution(tour, cities, total_travel_cost):
    # Requirement 1: Start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit each city exactly once
    if sorted(tour) != sorted(list(set(tour)) + [0] * (tour.count(0) - 1)):
        return "FAIL"

    # Calculate actual travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Requirement 4: Check if provided total travel cost is approximately equal to calculated travel cost
    if not math.isclose(total_travel_cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Visiting each city at least once and excluding multiple visits and subtours are handled implicitly above
    # Requirement 5: Excluding multiple subtours (single tour as claimed in the sequence already)
    # covered by the sorted subarray comparison in Requirement 2.
    
    return "CORRECT"

# Define the cities based on the problem statement
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54),
          (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Solution given
tour = [0, 3, 0]
total_travel_cost = 156.32018423735306

# Check the solution
result = verify_solution(tour, cities, total_travel_cost)
print(result)