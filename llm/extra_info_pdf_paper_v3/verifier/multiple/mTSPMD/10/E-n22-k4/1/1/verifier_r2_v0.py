import numpy as np

# Given cities coordinates (index corresponds to cities numbered from 0 to 21)
cities_coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Provided tours and respective travel costs
robot_tours = [
    [0, 8, 7, 10, 6, 16, 0],
    [1, 13, 17, 20, 15, 5, 1],
    [2, 14, 12, 18, 4, 2],
    [3, 11, 21, 19, 9, 3]
]

robot_costs = [124.13, 178.12, 194.72, 181.11]
overall_cost = 678.07

# Check requirements
def check_start_end_depot(tour, depot):
    return tour[0] == depot and tour[-1] == depot

def calculate_euclidean_distance(point1, point2):
    return np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def check_tours_and_costs():
    all_visited = set()
    calculated_overall_cost = 0
    depots = [0, 1, 2, 3]
    
    for robot_id, tour in enumerate(robot_tours):
        if not check_start_end_depot(tour, depots[robot_id]):
            return "FAIL: Tour does not start/end at assigned depot for robot {}".format(robot_id)
        
        # Calculate travel cost for the tour
        accumulated_cost = 0
        for i in range(len(tour) - 1):
            distance = calculate_euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
            accumulated_cost += distance
        
        if not np.isclose(accumulated_cost, robot_costs[robot_id], rtol=1e-03):
            return "FAIL: Reported cost does not match calculated cost for robot {}".format(robot_id)
        
        calculated_overall_cost += accumulated_cost
        
        # Add visited cities
        all_visited.update(tour[:-1])  # Exclude the depot return in final counter
    
    if all_visited != set(cities_coordinates.keys()):
        return "FAIL: Not all cities are visited exactly once."
    
    if not np.isclose(calculated_overall_cost, overall_cost, rtol=1e-03):
        return "FAIL: Overall cost does not match the summed individual costs."
    
    return "CORRECT"

result = check_tours_and_costs()
print(result)