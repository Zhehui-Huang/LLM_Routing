import math

def calculate_euclidean_distance(p1, p2):
    """Calculates the Euclidean distance between two points p1 and p2."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tours, cities_coordinates, expected_costs, overall_total_cost):
    city_visits = [0] * len(cities_coordinates)
    total_calculated_cost = 0
    
    for robot_id, tour in enumerate(tours):
        start_city = tour[0]
        end_city = tour[-1]
        
        # Check if each tour starts and ends at the robot's assigned depot
        if start_city != end_city or start_city != robot_id:
            return "FAIL"
        
        tour_cost = 0
        
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            
            # Accumulate visits to each city
            city_visits[city_from] += 1
            
            # Calculate travel cost between cities
            distance = calculate_euclidean_distance(cities_coordinates[city_from], cities_coordinates[city_to])
            tour_cost += distance
            
        # Consider the return to the initial city
        city_visits[end_city] += 1
        
        # Check if the tour cost matches expected cost within a tolerance due to rounding in provided values
        if not math.isclose(tour_cost, expected_costs[robot_id], rel_tol=1e-2):
            return "FAIL"
        
        total_calculated_cost += tour_cost
    
    # Check if each city is visited exactly once
    if any(visit != 1 for visit in city_visits):
        return "FAIL"
    
    # Check overall costs
    if not math.isclose(total_calculated_cost, overall_total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Test the input solution
cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Input tours and costs
tours = [
    [0, 14, 16, 17, 20, 18, 0],
    [1, 6, 8, 10, 12, 21, 1],
    [2, 5, 7, 9, 15, 2],
    [3, 4, 11, 13, 19, 3]
]

expected_costs = [79.20, 174.75, 107.52, 130.87]
overall_total_cost = 492.33

# Execute the test
test_result = verify_solution(tours, cities_coordinates, expected_costs, overall_total_cost)
print(testeer_result)