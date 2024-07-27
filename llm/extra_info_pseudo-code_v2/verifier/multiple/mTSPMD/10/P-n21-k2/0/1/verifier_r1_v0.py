import math

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def validate_solution(tours, costs, coords, overall_cost):
    # [Requirement 5]
    if len(coords) != 21:
        return "FAIL"
    
    all_visited_cities = set()
    total_calculated_cost = 0
    
    for i, tour in enumerate(tours):
        # [Requirement 6]
        if tour[0] != tour[-1]:
            return "FAIL"
        
        # [Requirement 3]
        if tour[0] != i:
            return "FAIL"
        
        # Calculate the cost of the current tour
        tour_cost = 0
        for j in range(len(tour) - 1):
            tour_cost += calculate_euclidean_distance(coords[tour[j]], coords[tour[j+1]])
        
        # [Requirement 1]
        if not math.isclose(tour_cost, costs[i], abs_tol=0.01):
            print(f"Tour cost match error: Expected {costs[i]}, Got {tour_cost}")
            return "FAIL"
        
        # Collects cities for [Requirement 2]
        all_visited_cities.update(tour[1:-1])
        
        # accumulate the tour cost for overall cost validation
        total_calculated_cost += tour_cost
    
    # Checking if all cities except depots are visited exactly once
    if len(all_visited_cities) != 19:
        return "FAIL"
    
    # [Requirement 7]
    if not math.isclose(total_calculated_cost, overall_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Provided tours and costs
robot_0_tour = [0, 0, 16, 10, 4, 11, 15, 12, 3, 8, 18, 19, 13, 2, 7, 5, 14, 17, 9, 20, 6, 0, 0]
robot_0_cost = 196.39
robot_1_tour = [1, 16, 1, 10, 4, 11, 15, 12, 3, 8, 18, 19, 13, 2, 7, 5, 14, 17, 9, 20, 6, 1]
robot_1_cost = 175.80

# Overall given travel cost
overall_given_cost = 197.84

# Perform validation
result = validate_solution(
    [robot_0_tour, robot_1_tour],
    [robot_0_cost, robot_1_cost],
    city_coords,
    overall_given_cost
)

print(result)