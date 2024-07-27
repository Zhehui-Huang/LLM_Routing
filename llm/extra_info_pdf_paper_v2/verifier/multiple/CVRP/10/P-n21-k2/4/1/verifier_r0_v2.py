import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_tour_and_cost(robot_tour, robot_travel_cost, coordinates, demand, capacity):
    total_demand = 0
    calculated_cost = 0
    current_load = 0
    last_city = robot_tour[0]

    for city in robot_tour[1:]:
        # Calculate the travel cost
        calculated_cost += calculate_euclidean_distance(*coordinates[last_city], *coordinates[city])
        last_city = city

        # Accumulate demand and check capacity only if not returning to depot
        if city != 0:
            current_load += demand[city]
            total_demand += demand[city]
            if current_load > capacity:
                return False, 0, 0
        
        # Reset load when returning to depot
        if city == 0:
            current_load = 0

    # Check for final return to depot not covered in loop
    calculated_cost += calculate_euclidean_distance(*coordinates[last_city], *coordinates[0])

    # Rounding errors in float comparison might require tolerance
    if abs(calculated_cost - robot_travel_cost) > 1e-2:
        return False, 0, 0

    return True, total_demand, calculated_cost

def unit_test_solution(robot_tours_data, coordinates, demands, capacity):
    total_calculated_cost = 0
    all_demands_met = set()

    for robot_tour, robot_travel_cost in robot_tours_data:
        valid, total_demand, calculated_cost = check_tour_and_cost(robot_tour, robot_travel_cost, coordinates, demands, capacity)
        
        if not valid:
            return "FAIL"
        
        total_calculated_cost += calculated_cost
        # Collect visited cities excluding depot (id=0)
        all_demands_met.update([city for city in robot_tour if city != 0])

    # Check all cities are covered correctly and all demand is met
    complete_city_coverage = set(range(1, len(coordinates))) == all_demands_met

    return "CORRECT" if complete_city_coverage else "FAIL"

# Robot tours and costs from your solution output
robot_0_tour = [0, 11, 9, 14, 0, 17, 13, 0, 15, 19, 0, 18, 8, 3, 12, 0]
robot_0_cost = 387.86
robot_1_tour = [0, 6, 1, 4, 2, 5, 0, 7, 20, 10, 16, 0]
robot_1_cost = 172.51

robot_tours_data = [
    (robot_0_tour, robot_0_cost),
    (robot_1_tour, robot_1_cost)
]

coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
               (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Run the test
result = unit_test_solution(robot_tours_data, coordinates, demands, 160)
print(result)