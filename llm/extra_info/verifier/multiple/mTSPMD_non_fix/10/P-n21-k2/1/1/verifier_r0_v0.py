import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

def verify_solution():
    cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
              (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
              (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
    
    tours = {
        0: [0, 16, 10, 4, 12, 18, 8, 2, 6, 20, 14],
        1: [1, 7, 5, 17, 9, 13, 19, 3, 15, 11]
    }

    total_costs = {
        0: 117.91958338162735,
        1: 111.39890596728392
    }
    
    reported_overall_cost = 229.31848934891127
    calculated_overall_cost = 0

    all_visited_cities = set()

    for robot_id, tour in tours.items():
        cost_calculated = 0
        tour_length = len(tour)
        for i in range(tour_length - 1):
            start_city = tour[i]
            end_city = tour[i + 1]
            cost_calculated += calculate_distance(cities[start_city], cities[end_city])
            all_visited_cities.add(start_city)
            all_visited_cities.add(end_city)
        
        if (cst := round(cost_calculated, 5)) != round(total_costs[robot_id], 5):
            print(f"FAIL: Calculated cost {cst} for Robot {robot_id} does not match the reported cost {total_costs[robot_id]}")
            return "FAIL"
        
        calculated_overall_cost += cost_calculated

    if len(all_visited_cities) != 21 or min(all_visited_cities) != 0 or max(all_visited_cities) != 20:
        print("FAIL: Not all cities have been visited exactly once.")
        return "FAIL"
    
    if round(calculated_overall_cost, 5) != round(reported_overall_cost, 5):
        print(f"FAIL: Calculated overall travel cost {calculated_overall_cost} does not match the reported cost {reported_overall_cost}")
        return "FAIL"
    
    return "CORRECT"

# Execute unit test
print(verify_solution())