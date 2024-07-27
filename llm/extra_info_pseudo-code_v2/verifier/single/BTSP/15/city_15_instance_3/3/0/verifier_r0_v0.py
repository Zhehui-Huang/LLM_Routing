import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_travel_cost, max_distance):
    cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
              (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]
    
    # [Requirement 1] Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Each city must be visited exactly once
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # CALCULATED TOTAL TRAVEL COST AND MAXIMUM DISTANCE:
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour)-1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_cost += distance
        if distance > calculated_max distance:
            calculated_max_distance = distance
    
    # [Requirement 6] Check if total travel cost is accurate
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    # [Requirement 7] Check if maximum distance between any two consecutive cities is accurate
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Example solution provided
example_tour = [0, 6, 13, 10, 9, 5, 14, 8, 11, 2, 7, 3, 12, 4, 1, 0]
example_total_travel_cost = 317.24
example_max_distance = 48.37

# Testing the example solution
result = test_solution(example_tour, example_total_travel_cost, example_max_distance)
print(result)