import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def test_solution():
    cities_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
        15: (37, 69)
    }
    demands = {
        1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 8, 10: 8,
        11: 7, 12: 14, 13: 6, 14: 19, 15: 11
    }
    robot_tours = [
        [0, 9, 13, 0], [0, 12, 15, 0], [0, 6, 0], [0, 4, 11, 0],
        [0, 5, 14, 0], [0, 3, 0], [0, 1, 10, 0], [0, 2, 0]
    ]
    robot_capacities = [35] * 8
    total_travel_cost_check = 427.37
    actual_total_travel_cost = 0

    # Check if each tour starts and ends at the depot
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Check demands are met and capacity constraints are adhered to
    city_served = {i: 0 for i in demands}
    for idx, tour in enumerate(robot_tours):
        current_load = 0
        previous_city = tour[0]
        for city in tour[1:]:
            if city != 0:  # Don't count the depot in demand delivery
                city_served[city] += demands[city]
                current_load += demands[city]
            if current_load > robot_capacities[idx]:
                return "FAIL"
            actual_total_travel_cost += calculate_distance(cities_coordinates[previous_city], cities_coordinates[city])
            previous_city = city
        actual_total_travel_cost += calculate_distance(cities_coordinates[previous_city], cities_coordinates[0])

    # Verifying that all demands are fully met
    for city, demand in demands.items():
        if demand != city_served[city]:
            return "FAIL"
    
    # Verify the total travel cost
    if not math.isclose(actual_total_travel_cost, total_travel_cost_check, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Call the test function
result = test_solution()
print(result)