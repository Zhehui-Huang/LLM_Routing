import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def verify_solution(robot_tours, tour_costs, overall_cost):
    # Coordinates for cities index 0 to 20:
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
        (45, 35)
    ]
    
    # Combine all tours
    all_visited = [city for tour in robot_tours for city in tour]
    unique_visited = set(all_visited)
    
    # Check if all cities from 0 to 20 are visited exactly once
    requirement_1 = len(all_visited) == len(unique_visited) == 21
    
    # Check if each tour starts and ends on depot 0 for this solution (Requirement 2)
    requirement_2 = all(tour[0] == 0 for tour in robot_tours)
    
    # Compute travel costs and check with provided costs
    computed_costs = []
    for tour in robot_tours:
        cost = sum(calculate_distance(coordinates[tour[i]][0], coordinates[tour[i]][1],
                                      coordinates[tour[i+1]][0], coordinates[tour[i+1]][1]) for i in range(len(tour)-1))
        computed_costs.append(cost)
    
    # Check if the calculated travel costs match the provided costs (Requirement 3)
    requirement_3 = all(abs(computed - provided) < 0.01 for computed, provided in zip(computed_proposed_costs, cost_list))
    
    # Check if the total cost matches the overall provided cost (Requirement 4)
    requirement_4 = abs(sum(computed_costs) - overall_cost) < 0.01

    if all([requirement_1, requirement_2, requirement_3, requirement_4]):
        return "CORRECT"
    else:
        return "FAIL"

# Data from your solution
robot_tours = [
    [0, 20, 7, 5, 14, 17, 9, 6, 2, 19],
    [0, 16, 10, 4, 11, 3, 8, 13, 18, 12, 15]
]
tour_costs = [112.34804464171299, 125.44216939015841]
overall_cost = 237.79021403187141

# Verify if the proposed solution is correct
result = verify_solution(robot_tours, tour_costs, overall_cost)
print("Result of verification:", result)