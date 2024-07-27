import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tours, coordinates):
    def calculate_total_travel_cost(tour):
        total_cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i+1]
            total_cost += euclidean_distance(*coordinates[city1], *coordinates[city2])
        return total_cost
    
    total_combined_cost = 0
    visited_cities = set()
    
    # Check each robot tour
    for robot_id, tour in tours.items():
        if tour[0] != tour[-1]:
            return "FAIL", "Start and end depot does not match for Robot {}".format(robot_id)
        
        start_depot = tour[0]
        if not (start_deput == robot_id):
            return "FAIL", "Robot does not start at its assigned depot"
        
        visited_cities.update(tour)
        
        tour_cost = calculate_total_travel_cost(tour)
        if tours[robot_id]["cost"] != round(tour_cost, 2):
            return "FAIL", "Incorrect travel cost for Robot {}".format(robot_id)
        
        total_combined_cost += tour_cost

    if len(visited_cities) != 21:
        return "FAIL", "Not all cities are visited exactly once"

    if abs(total_combined_cost - sum(tour["cost"] for tour in tours.values())) > 0.01:
        return "FAIL", "Overall travel cost discrepancy"

    return "CORRECT", f"Overall Total Travel Cost: {total_combined_cost}"

# Solution details
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

robot_tours = {
    0: {"tour": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0], "cost": 262.97},
    1: {"tour": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 1], "cost": 288.84}
}

# Verification
verification_result, message = verify_solution(robot_tours, cities_coordinates)
print(verification_result)