import math

# Mock data as given example does not have all the required fields
cities = {
    0: (145, 215), # depot for robot 0
    1: (151, 264), # depot for robot 1
    2: (159, 261), # depot for robot 2
    3: (130, 254), # depot for robot 3
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def check_tours(tours, depots, cities):
    visited = set()
    total_travel_cost = 0.0
    all_costs = []

    for i, tour in enumerate(tours):
        if tour[0] != depots[i] or tour[-1] != depots[i]:
            return "FAIL: Robot does not start or end at its assigned depot", 0
        
        tour_cost = 0
        for j in range(len(tour) - 1):
            tour_cost += euclidean_distance(cities[tour[j]], cities[tour[j+1]])
            if tour[j+1] in visited and tour[j+1] not in depots:
                return "FAIL: City visited more than once", 0
            visited.add(tour[j+1])

        all_costs.append(tour_cost)
        total_travel_cost += tour_cost
        
        if set(tour) - {depots[i]} == {depots[i]}:
            return "FAIL: Robot did not visit any city", 0

    if visited != set(cities.keys()):
        return "FAIL: Not all cities are visited", 0

    if len(tours) != 4:
        return "FAIL: Incorrect number of robot tours", 0

    return "CORRECT", total_travel_cost

# Example output in the original task description
robot_tours = [
    [0, 8, 12, 10, 7, 9, 0],  # Fixed based on your example for correctness
    [1, 12, 13, 11, 6, 9, 1],
    [2, 9, 11, 8, 10, 2],
    [3, 15, 11, 12, 13, 3]
]

depots = [0, 1, 2, 3]

result, total_cost = check_tours(robot_tours, depots, cities)
print(result)
if result == "CORRECT":
    print(f"Reported Overall Total Travel Cost: 315.04")
    print(f"Calculated Overall Total Travel Cost: {total_cost}")