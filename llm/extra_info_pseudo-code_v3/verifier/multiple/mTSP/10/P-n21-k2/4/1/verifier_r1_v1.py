import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_path_cost(tour, coordinates):
    total_cost = 0.0
    for i in range(1, len(tour)):
        x1, y1 = coordinates[tour[i - 1]]
        x2, y2 = coordinates[tour[i]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    return total_cost

def verify_solution(robot_tours, robot_costs, overall_claimed_cost):
    coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
                   (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
                   (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
                   (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
                   (45, 35)]

    all_cities_visited = set()
    computed_costs = []
    
    for tour, claimed_cost in zip(robot_tours, robot_costs):
        # Check if tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check if all cities are visited exactly once except depot
        for city in tour[1:-1]:
            if city in all_cities_visited:
                return "FAIL"
            all_cities_visited.add(city)
    
        # Check the calculated cost against claimed cost
        calculated_cost = total_path_cost(tour, coordinates)
        computed_costs.append(calculated_cost)
        if not math.isclose(calculated_cost, claimed_cost, rel_tol=1e-2):
            return "FAIL"
    
    computed_overall_cost = sum(computed_costs)
    
    # Check if overall cost matches
    if not math.isclose(computed_overall_cost, overall_claimed_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Ensure all cities except the depot have been visited
    if all_cities_visited != set(range(1, 21)):
        return "FAIL"

    return "CORRECT"

# Given solution
robot_0_tour = [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0]
robot_0_cost = 135.57
robot_1_tour = [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
robot_1_cost = 160.83
overall_claimed_cost = 296.40

# Test the verification function
result = verify_solution(
    [robot_0_tour, robot_1_tour],
    [robot_0_cost, robot_1_cost],
    overall_claimed_cost
)

print(result)