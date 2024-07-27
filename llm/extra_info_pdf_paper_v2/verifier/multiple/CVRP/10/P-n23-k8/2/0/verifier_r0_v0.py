import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tours(tours, cities, demands, robots_capacity):
    total_demand_fulfilled = [0] * len(demands)
    total_travel_cost = 0
    
    # Check if all tours start and end at the depot city 0
    satisfy_start_end_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)
    
    if not satisfy_start_end_depot:
        return "FAIL: Tours do not start and end at depot"

    # Check if any tour exceeds the robot capacity and calculate total demands
    for tour in tours:
        load = 0
        prev_city_idx = tour[0]
        for city_idx in tour[1:]:
            load += demands[city_idx]
            total_demand_fulfilled[city_idx] += demands[city_idx]
            # Calculate travel cost
            total_travel_cost += calculate_distance(cities[prev_city_idx], cities[city_idx])
            prev_city_idx = city_idx
            if load > robots_capacity:
                return "FAIL: Robot capacity exceeded"
        # Include travel back to the depot in the travel cost
        total_travel_modes_factoring_back_to_depot = calculate_distance(cities[prev_city_idx], cities[0])
        total_travel_cost += total_travel_modes_factoring_back_to_depot

    # Check if all demands are fulfilled
    if not all(fulfilled == demand for fulfilled, demand in zip(total_demand_fulfilled, demands)):
        return "FAIL: City demands not all met"
    
    # Check if exactly 8 robots are used
    if len(tours) != 8:
        return "FAIL: Incorrect number of robots used"
    
    # Check if every city except depot is included in tours
    included_cities = set(city for tour in tours for city in tour[1:-1])
    if included_cities != set(range(1, len(demands))):
        return "FAIL: Not all cities are visited"

    return "CORRECT"

# Example to test the functions - This section should be replaced with real route solutions.

cities = {
    0: (30, 40),
    1: (37, 52),
    # City coordinates continue...
}
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robots_capacity = 40

# Example Tours (These should be the output from the optimized CVRP algorithm)
example_tours = [
    [0, 1, 2, 3, 0],
    [0, 4, 5, 0],
    # More tours...
]

# Run the validation
print(validate_tours(example_tours, cities, demands, robots_capacity))