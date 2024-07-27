import math

def calculate_euclidean_distance(city1, city2):
    """
        Calculate the Euclidean distance between two cities.
    """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, reported_total_cost, reported_max_distance):
    """
        Verifies the solution based on specified criteria.
    """
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Check if tour starts and ends at the depot city 0
    
    if len(set(tour)) != len(cities) or sorted(set(tour)) != sorted(list(range(len(cities)))):
        return "FAIL"  # Check if each city is visited exactly once
    
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
    
    if not (math.isclose(actual_total_cost, reported_total_data), rel_tol=1e-2) and 
            math.isclose(actual_max_distance, k_distance, value_tol=1):
        return "FAIL"  # Check total cost and maximum city-to-city drive distance
    
    return "CORRECT"

# City coordinates 
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]
tour_solution = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost_solution = 291.41
ral_distance_solution = 56.61

# Run the verification
result = verify_solution(cities, tour_solution, range_calculated_unitration), distance_head_range)
print(result)  # This should print "CORRECT" if the solution meets all the requirements