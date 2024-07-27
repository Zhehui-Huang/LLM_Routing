import math

# Definition of cities and their coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Definition of demands for each city
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Tours and costs given by your results
robot_tours = [
    [0, 6, 0], [0, 1, 10, 13, 0], [0, 2, 0], [0, 4, 11, 0],
    [0, 7, 5, 9, 0], [0, 15, 12, 0], [0, 14, 3, 0], [0, 8, 0]
]

robot_costs = [24.08, 68.44, 42.05, 57.39, 75.54, 66.12, 100.91, 64.90]

def calculate_distance(p1, p2):
    """ Utility to calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Check constraints
def check_solution(tours, costs, demands, coordinates, capacity=35):
    total_cost_calculated = 0
    all_cities_covered = set(range(1, 16))  # City 0 is depot and does not need to be covered
    max_capacity = capacity
    for tour, reported_cost in zip(tours, costs):
        current_cost = 0
        current_load = 0
        last_city = tour[0]
        for city in tour[1:]:
            # Calculate travel cost and load
            current_cost += calculate_distance(coordinates[last_city], coordinates[city])
            current_load += demands[city]
            last_city = city
            if city != 0:  # Exclude the depot city for demand fulfillment
                all_cities_covered.discard(city)
        # Add return cost to depot (from last city in tour)
        current_cost += calculate_distance(coordinates[last_city], coordinates[0])
        total_cost_calculated += current_cost
        # Check if the reported cost matches the calculated cost
        if not math.isclose(current_cost, reported_cost, abs_tol=0.01):
            print(f"Cost mismatch: reported {reported_cost}, calculated {current_cost}")
            return "FAIL"
        # Check capacity constraint
        if current_load > max_capacity:
            print(f"Capacity exceeded: {current_load} > {max_capacity}")
            return "FAIL"

    # Check if all city demands are met
    if all_cities_covered:
        print("Not all cities were covered.")
        return "FAIL"
    # Check if total cost is reported correctly
    if not math.isclose(sum(robot_costs), total_cost_calculated, abs_tol=0.01):
        print(f"Total cost mismatch: reported {sum(robot_costs)}, calculated {total_cost_calculated}")
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = check_solution(robot_tours, robot_costs, city_demands, city_coordinates)
print(result)