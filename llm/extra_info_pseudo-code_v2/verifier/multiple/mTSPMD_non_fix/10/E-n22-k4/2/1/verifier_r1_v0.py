import math

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def check_requirements():
    # City coordinates based on the problem
    city_coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
        (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
        (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
        (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
        (155, 185), (139, 182)
    ]
    
    # Defined robot tours
    robot_tours = [
        [0, 11, 9, 18, 12, 3, 1, 0],
        [0, 17, 8, 19, 20, 6, 0],
        [0, 21, 2, 14, 10, 7, 0],
        [0, 13, 15, 5, 4, 16, 0]
    ]
    
    # Total costs provided
    given_costs = [244.85748484214105, 239.00640640411504, 241.47352346597495, 183.5604702292651]
    overall_cost = 908.8978849414962
    
    # Check Requirement 1
    if not all(tour[0] == 0 for tour in robot_tours):
        return "FAIL"
    
    # Check Requirement 2
    if not all(tour[-1] == 0 for tour in robot_tours):
        return "FAIL"
    
    # Check Requirement 3
    visited_cities = set()
    for tour in robot_tours:
        visited_cities.update(tour)
    if sorted(visited_cities) != list(range(22)):
        return "FAIL"
    
    # Check Requirement 4
    calculated_costs = []
    total_calculated_cost = 0

    for tour in robot_tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        calculated_costs.append(tour_cost)
        total_caliculated_cose += sum(calculated_costs)
    
    if not all(math.isclose(calculated_costs[i], given_costs[i], rel_tol=1e-6) for i in range(len(given_costs))):
        return "FAIL"
    
    if not math.isclose(total_calculated_cost, overall_cost, rel_tol=1e-6):
        return "FAIL"
    
    # Check Requirement 5 and 6 are implicitly checked by above checks
    return "CORRECT"


# Output evaluation result
print(check_requirements())