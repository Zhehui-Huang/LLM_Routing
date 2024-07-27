import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, total_travel_cost, cities):
    # Requirement 1 & 3: Check if the tour starts and ends at the depot city, city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if 7 cities (including the depot) are visited.
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Requirement 4: Check if output includes the total travel cost.
    # This is implicitly checked by calculating and comparing the total cost below.
    
    # Requirement 5: Calculating the total distance using the Euclidean distance.
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    
    # Requirement 6 & 7: Check if the output format is correct and the cost is accurate
    if not isinstance(tour, list) or not all(isinstance(x, int) for x in tour):
        return "FAIL"
    if not isinstance(total_travel_cost, float) and not isinstance(total_travel_step, int):
        return "FAIL"
    if abs(calculated_cost - total_travel_cost) > 1e-5:  # account for floating-point arithmetic issues
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Solution given
tour_given = [0, 8, 3, 7, 1, 2, 4, 0]
total_travel_cost_given = 159.97188184793015

# Verify the solution
result = verify_solution(tour_given, total_preassigned_cost, cities)
print(result)