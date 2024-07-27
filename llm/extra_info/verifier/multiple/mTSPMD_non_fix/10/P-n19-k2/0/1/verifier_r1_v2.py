import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(robot_tours, total_costs, overall_total_cost):
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    all_visited_cities = set()
    computed_overall_cost = 0
    for idx, tour in enumerate(robot_tours):
        if tour[0] != 0 or (len(tour) > 1 and tour[-1] not in {0, 1}):
            return "FAIL"
        if len(set(tour)) + len(all_visited_cities) > len(set(tour).union(all_visited_cities)):
            return "FAIL"
        all_visited_cities.update(tour)

        # Calculate tour's travel cost
        computed_cost = 0
        for j in range(1, len(tour)):
            computed_cost += calculate_euclidean_distance(coordinates[tour[j - 1]], coordinates[tour[j]])

        if not math.isclose(computed_cost, total_costs[idx], abs_tol=0.01):
            return "FAIL"
        
        computed_overall_cost += computed_cost

    if len(all_visited_cities) != len(coordinates):
        return "FAIL"
    
    if not math.isclose(computed_overall_cost, overall_total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"


# Provided solution data
robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 8, 16, 17, 3, 12, 14, 4, 11, 10]
robot_1_tour = [1]
robot_tours = [robot_0_tour, robot_1_tour]
total_costs = [173.53, 0.00]
overall_total_cost = 173.53

# Validating the solution
print(verify_solution(robot_tours, total_costs, overall_total_cost))