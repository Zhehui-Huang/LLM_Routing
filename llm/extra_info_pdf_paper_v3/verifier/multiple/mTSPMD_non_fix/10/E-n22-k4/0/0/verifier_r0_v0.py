import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates as provided
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Provided solution information
robots_tours = {
    0: [0, 18, 12, 9, 5, 11],
    1: [1, 4, 10, 14, 20, 21],
    2: [2, 6, 8, 16, 17],
    3: [3, 13, 19, 15, 7]
}

# Validate requirements
def is_correct_solution():
    visited_cities = set()
    total_calculated_cost = 0.0
    
    for robot_id, tour in robots_tours.items():
        # Check each tour starts with the robot's depot
        if tour[0] != robot_id:
            print(f"Robot {robotID} does not start at its designated depot.")
            return "FAIL"

        # Validate travel cost and collect visited cities
        robot_total_cost = 0.0
        for i in range(len(tour) - 1):
            robot_total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            visited_cities.add(tour[i])
        visited_cities.add(tour[-1])
        robot_total_cost += calculate_distance(cities[tour[-1]], cities[tour[0]])  # to simulate return to depot

        # Assume provided robot costs are accurate, so we calculate and check with a small epsilon error range
        if abs(robot_total_cost - provided_costs[robot_id]) > 1e-6:
            print(f"Robot {robotID} traveled cost is incorrect.")
            return "FAIL"
        
        total_calculated_cost += robot_total_cost

    # Check all cities visited exactly once
    if len(visited_cities) != len(cities):
        return "FAIL"

    # Calculate overall total cost and validate
    provided_total_cost = sum(provided_costs.values())
    if abs(provided_total_cost - total_calculated_cost) > 1e-6:
        return "FAIL"

    return "CORRECT"

# Cost from provided information
provided_costs = {
    0: 124.0993245299486,
    1: 119.28670261374883,
    2: 75.24466009129246,
    3: 138.96920988271688
}

print(is_correct_solution())