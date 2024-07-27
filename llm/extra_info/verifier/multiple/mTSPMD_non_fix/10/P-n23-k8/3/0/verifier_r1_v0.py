import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 
        18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
    }
    
    # Robot tours and costs provided in the solution
    robot_tours = [
        [0], [0], [0], [0], [0], [0], [0],
        [0, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 
         12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    ]
    robot_costs = [0, 0, 0, 0, 0, 0, 0, 0]
    
    # Calculate total costs from proposed solution
    def check_total_travel_cost(robot_tours, robot_costs):
        overall_cost_calculated = 0
        all_cities_visited = set()
        for robot_id, tour in enumerate(robot_tours):
            tour_cost = 0
            if len(tour) > 1:
                for i in range(len(tour) - 1):
                    tour_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
                    all_cities_visited.add(tour[i])
            # Last city in the last robot's tour
            all_cities_visited.add(tour[-1])
            
            print(f"Robot {robot_id} Calculated Tour Cost: {tour_cost:.2f}")
            if abs(tour_cost - robot_costs[robot_id]) > 0.1:  # allowing floating point tolerance
                return "FAIL: Cost mismatch"
            
            overall_cost_calculated += tour_cost
            
        if all_cities_visited != set(cities.keys()):
            return "FAIL: Not all cities visited exactly once"
        
        if overall_cost_calculated != sum(robot_costs):
            return "FAIL: Overall cost mismatch"
        
        return "CORRECT"
    
    return check_total_travel_cost(robot_tours, robot_costs)

# Run the test
print(test_solution())