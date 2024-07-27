import math

def calculate_distance(city1, city2):
    # Helper function to calculate Euclidean distance between two cities
    return math.sqrt((city1[0] - city2[1]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    # City coordinates including the depot city at index 0
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # Requirement 1: Visit each city exactly once and return to depot
    if len(set(tour)) != len(cities) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate actual costs and distances
    actual_cost = 0
    actual_max_distance = 0
    for i in range(len(tour)-1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        actual_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
    
    # Requirement 4: Check total travel cost
    if not math.isclose(actual_cost, total_cost, rel_tol=1e-3):
        return "FAIL"
    
    # Requirement 5: Check maximum distance between consecutive cities
    if not math.isclose(actual_max_distance, max_distance, rel_tol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 8, 17, 8, 0]
total_travel_cost = 12.81
maximum_distance = 6.40

# Run test
print(verify_solution(tour, total_travel_cost, maximum_distance))