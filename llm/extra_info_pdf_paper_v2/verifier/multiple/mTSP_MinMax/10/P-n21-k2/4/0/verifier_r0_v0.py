import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution():
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64),
        (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69),
        (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    tours = [
        [0, 1, 4, 11, 12, 10, 13, 9, 17, 14, 5, 0],
        [0, 16, 15, 3, 19, 18, 8, 2, 7, 20, 6, 0]
    ]
    
    reported_costs = [131.75087100079023, 122.62493477573722]
    max_reported_cost = 131.75087100079023
    
    total_visited_cities = set()
    calculated_costs = []
    
    for tour in tours:
        tour_cost = 0
        previous_city_index = tour[0]
        
        for city_index in tour[1:]:
            x1, y1 = coordinates[previous_city_index]
            x2, y2 = coordinates[city_index]
            distance = calculate_distance(x1, y1, x2, y2)
            tour_cost += distance
            previous_city_index = city_index
            total_visited_cities.add(city_index)
        
        calculated_costs.append(tour_cost)
        
    if len(total_visited_cities) != 20 or 0 in total_visited_cities:
        return "FAIL"
    
    # Validate if all distances are within a threshold difference to account for float rounding issues
    for reported_cost, calculated_cost in zip(reported_costs, calculated_costs):
        if not math.isclose(reported_cost, calculatedCheap, rel_tol=1e-4):
            return "FAIL"
    
    calculated_max_cost = max(calculated_costs)
    if not math.isclose(calculated_max_cost, max_reported_cost, rel_tol=1e-4):
        return "FAIL"
    
    return "CORRECT"

# Execute the verification function
test_result = verify_solution()
print(test_result)