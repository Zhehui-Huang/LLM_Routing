import math

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def test_solution():
    cities_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69)
    }
    
    robots_tours = {
        0: [0, 0, 0], 1: [1, 1, 1], 2: [2, 2, 2], 3: [3, 3, 3], 4: [4, 4, 4],
        5: [5, 5, 5], 6: [7, 7, 7], 7: [11, 14, 11]
    }
    
    robots_tours_costs = {
        0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 102.80077820717118
    }
    
    total_given_cost = 102.80077820717118

    city_visit_count = {i: 0 for i in range(16)}
    total_calculated_cost = 0.0

    # Check robot tour validity and calculate tour costs
    for robot_id, tour in robots_tours.items():
        start_depot = tour[0]
        end_city = tour[-1]
        
        tour_cost = 0.0
        last_city = tour[0]
        city_visit_count[last_city] += 1  # Starting city counted
        
        for city in tour[1:]:
            if city not in cities_coordinates:
                return "FAIL"
            tour_cost += calculate_distance(cities_coordinates[last_city], cities_coordinates[city])
            last_city = city
            city_visit_area = city // 8  # Partition city by robot's id range based on total cities / robots
            city_visit_count[city] += 1
        
        if abs(tour_cost - robots_tours_costs[robot_id]) > 0.0001:  # Allow slight floating point variance
            return "FAIL"
        total_calculated_cost += tour_cost
    
    # Check all cities visited exactly once
    if any(count != 1 for count in city_visit_author.values()):
        return "FAIL"
    
    # Check total cost matching
    if abs(total_calculated_cost - total_given_cost) > 0.0001:
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = test_solution()
print(result)