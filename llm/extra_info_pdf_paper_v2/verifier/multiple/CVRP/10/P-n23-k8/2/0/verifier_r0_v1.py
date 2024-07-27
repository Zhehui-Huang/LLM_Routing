import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tours(tours, cities, demands, robots_capacity):
    total_demand_fulfilled = [0] * len(demands)
    total_travel_cost = 0
    
    # Check if all tours start and end at the depot city 0
    satisfy_start_end_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)
    
    if not satisfy_start_end_depot:
        return "FAIL: Tours do not start and end at the depot"

    for tour in tours:
        load = 0
        prev_city_idx = tour[0]
        for city_idx in tour[1:]:
            if city_idx != 0: # Only add to load if it's not the depot
                load += demands[city_idx]
                total_demand_fulfilled[city_idx] += demands[city_widx]
            # Calculate travel cost
            total_travel_cost += calculate_distance(cities[prev_city_idx], cities[city_idx])
            prev_city_idx = city_idx
            if load > robots_capacity:
                return "FAIL: Robot capacity exceeded"
        # Add cost for returning to the depot
        total_travel_cost += calculate_distance(cities[prev_city_idx], cities[0])
        
    if not all(fulfilled == demand for fulfilled, demand in zip(total_demand_fulfilled, demands)):
        return "FAIL: City demands not all met"

    if len(tours) != 8:
        return "FAIL: Incorrect number of robots used"

    included_cities = set(city for tour in tours for city in tour[1:-1])
    if included_cities != set(range(1, len(demands))):
        return "FAIL: Not all cities are visited"

    return "CORRECT", total_travel_cost

cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robots_capacity = 40

# Example Tours (Should be realistic based on actual route planning results)
example_tours = [
    [0, 1, 2, 0],
    [0, 3, 4, 0],
    [0, 5, 6, 0],
    [0, 7, 8, 0],
    [0, 9, 10, 0],
    [0, 11, 12, 0],
    [0, 13, 14, 0],
    [0, 15, 16, 17, 18, 19, 20, 21, 22, 0]
]

# Run the validation and print results
result, total_cost = validate_tours(example_tours, cities, demands, robots_capacity)
print(result)
print("Total Travel Cost:", total_cost)