import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y1 - y2)**2)

def evaluate_solution(tour, cost, max_distance):
    # City Coordinates (depot included)
    city_coordinates = {
        0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
        4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
        8: (17, 69), 9: (95, 89)
    }
    
    # Check Requirement 1: Tour starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Each city is visited exactly once apart from the depot city
    unique_cities = set(tour)
    if len(unique_cities) != 10 or sorted(unique_cities) != list(range(10)):
        return "FAIL"
    
    # Check Requirement 5: Tour includes the depot beginning and end
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Calculate total travel cost and check maximum distance between consecutive cities
    actual_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i+1]]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        actual_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
    
    # Check Requirement 3: Use Euclidean distance (implicitly checked by using calculate_euclidean_distance)
    
    # Check Requirement 6: Total travel cost matches the provided
    if not math.isclose(actual_cost, cost, abs_tol=0.01):
        return "FAIL"

    # Check Requirement 7: Correct maximum distance between consecutive cities
    if not math.isclose(actual_max_distance, max_distance, abs_tol=0.01):
        return "FAIL"

    # If all checks passed:
    return "CORRECT"
    
# Provided solution details
provided_tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
provided_cost = 291.41
provided_max_distance = 56.61

# Evaluate the solution
result = evaluate_solution(provided_tour, provided_cost, provided_max_distance)
print(result)