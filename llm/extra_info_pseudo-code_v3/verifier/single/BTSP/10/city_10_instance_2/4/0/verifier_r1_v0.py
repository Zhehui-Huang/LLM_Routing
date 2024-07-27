import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, max_distance):
    # Define cities based on the problem statement
    cities = [
        (90, 3), (11, 17), (7, 27), (95, 81), (41, 54),
        (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
    ]
    
    # Verify Requirement 5: tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 2: each city is visited exactly once, plus start/end at city 0
    if set(tour) != set(range(len(cities))):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance between consecutive cities
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        calculated_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)
    
    # Verify Requirement 6: total travel cost is accounted
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-6):
        return "FAIL"
    
    # Verify Requirement 7: the maximum distance is accounted
    if not math.isclose(calculated_max_distance, max_distance, abs_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Example of usage:
# Assuming there is a hypothetical solution
hypothetical_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hypothetical_total_cost = 300
hypothetical_max_distance = 50

# Verify the solution based on these hypothetical values
result = verify_solution(hypothetical_tour, hypothetical_total_cost, hypothetical_max_distance)
print(result)