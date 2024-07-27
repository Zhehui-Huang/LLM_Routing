import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(robot_tours, total_costs, overall_total_cost):
    # City coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Checking if cities are visited exactly once and all cities are visited
    all_visited_cities = set()
    for tour in robot_tours:
        if not tour:  # make sure no empty tour
            print("FAIL: Empty tour detected.")
            return "FAIL"
        # Check if the tour starts with the robot's depot
        if tour[0] != tour[-1] or (tour[0] != 0 and tour[0] != 1):
            print(f"FAIL: Robot tour does not end or start appropriately. Tour: {tour}")
            return "FAIL"
        tour_cities = set(tour)
        if len(tour_cities.intersection(all_visited_cities)) > 0:
            print("FAIL: City visited more than once between all robots.")
            return "FAIL"
        all_visited_cities.update(tour_cities)
    
    if len(all_visited_cities) != len(coordinates):
        print("FAIL: Not all cities visited.")
        return "FAIL"
    
    # Check if the total_costs length matches the robot_tours length
    if len(total_costs) != len(robot_tours):
        print("FAIL: Total costs do not match number of robots.")
        return "FAIL"

    # Verify total costs and distances
    computed_overall_cost = 0
    for idx, tour in enumerate(robot_tours):
        computed_cost = 0
        
        for city_index in range(1, len(tour)):
            computed_cost += calculate_euclidean_distance(
                coordinates[tour[city_index - 1]], coordinates[tour[city_index]]
            )
        
        if not math.isclose(computed_cost, total_costs[idx], abs_tol=0.01):
            print(f"FAIL: Computed tour cost does not match provided cost. Expected: {total_costs[idx]}, Computed: {computed_cost}")
            return "FAIL"
        
        computed_overall_cost += computed_cost

    if not math.isclose(computed_overall_task, overall_total_cost, abs_tol=0.01):
        print(f"FAIL: Overall computed cost does not match provided overall cost. Expected: {overall_total_cost}, Computed: {computed_overall_cost}")
        return "FAIL"

    return "CORRECT"

# Provided solution data
robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 8, 16, 17, 3, 12, 14, 4, 11, 10]
robot_1_tour = [1]
robot_tours = [robot_0_tour, robot_1_tour]
total_costs = [173.53, 0.00]
overall_total_cost = 173.53

# Verify solution correctness
print(verify_solution(robot_tours, total, combined_total_cost))