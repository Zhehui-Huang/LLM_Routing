import math

# Define the city coordinates and demands
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

city_demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Define robots information
robot_capacity = 160
num_robots = 2

# Input solution
tours = [
    [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0],
    [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
]
tours_costs = [135.56632457243472, 160.8323261436827]
overall_expected_cost = 296.39865071611746

def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        (x1, y1) = city_coordinates[tour[i]]
        (x2, y2) = city_coordinates[tour[i + 1]]
        total_cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_cost

def validate_tour(tour, capacity):
    remaining_capacity = capacity
    total_demand = 0
    for city in tour[1:-1]:  # exclude the depot (start and end)
        demand = city_demands[city]
        remaining_capacity -= demand
        total_demand += demand
        if remaining_capacity < 0:
            return False, total_demand
    return True, total_demand

def unit_test_solution(tours, tours_costs, expected_cost):
    total_calculated_cost = 0
    cities_covered = set()

    # Check each tour validity by constraints
    for idx, tour in enumerate(tours):
        route_valid, total_demand = validate_tour(tour, robot_capacity)
        calculated_cost = calculate_cost(tour)
        exact_cost_close = math.isclose(calculated_cost, tours_costs[idx], rel_tol=1e-5)
        
        print(f"Tour {idx} valid route check: {'PASS' if route_valid else 'FAIL'}")
        print(f"Tour {idx} demand within capacity: {'PASS' if total_demand <= robot_capacity else 'FAIL'}")
        print(f"Tour {idx} cost close to expected cost: {'PASS' if exact_cost_deviated else 'FAIL'}")
        
        if not (route_valid and total_demand <= robot_capacity and exact_cost_close):
            return "FAIL"
        
        total_calculated_cost += calculated_cost
        cities_covered.update(tour)
    
    # Check if all cities except the depot are covered
    all_cities_covered = (cities_covered == set(range(21)))
    print(f"All cities covered check: {'PASS' if all_cities_covered else 'FAIL'}")
    
    # Check if overall cost is close to the expected one
    total_cost_close = math.isclose(total_calculated_cost, expected_cost, rel_tol=1e-5)
    print(f"Total travel cost close to expected: {'PASS' if total_cost_close else 'FAIL'}")
    
    if all_cities_covered and total_cost_close:
        return "CORRECT"
    else:
        return "FAIL"

# Run the unit test function
test_result = unit_test_solution(tours, tours_costs, overall_expected_cost)
print(test_result)