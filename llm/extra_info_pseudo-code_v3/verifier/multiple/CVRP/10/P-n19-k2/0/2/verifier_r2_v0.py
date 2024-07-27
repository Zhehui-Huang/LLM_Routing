import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, costs, cities, demands, capacity):
    total_cost_calculated = 0
    all_cities_visited = set()

    # Verify each robot's path and costs:
    for robot_id, tour in enumerate(tours):
        # Check round-trip to depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        current_capacity = 0
        for i in range(len(tour) - 1):
            from_city = tour[i]
            to_city = tour[i + 1]
            current_capacity += demands[to_city]
            
            # Calculate distance between cities
            dist = calculate_distance(cities[from_city], cities[to_city])
            total_cost_calculated += dist

            # Add visited city (excluding depot)
            if to_city != 0:
                all_cities_visited.add(to_city)

            # Check capacity constraints
            if current_capacity > capacity:
                return "FAIL"
        
        # Check if the cost matches
        if not math.isclose(total_cost_calculated, costs[robot_id], abs_tol=1e-2):
            return "FAIL"

        # Reset for next tour
        current_capacity = 0
    
    # Check if all demands have been satisfied
    if all_cities_visited != set(range(1, len(cities))):
        return "FAIL"

    # Check if provided total cost matches computed cost
    if not math.isclose(sum(costs), overall_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided data
cities_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160

# Solution provided
tours = [
    [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
    [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
]
costs = [129.15, 172.59]
overall_cost = 301.75

# Validate solution
result = verify_solution(tours, costs, cities_coordinates, demands, robot_capacity)
print(result)