import numpy as np

# Provided robot tours and costs
robot_tours = [
    [0, 21, 1, 10],
    [0, 16, 2, 7],
    [0, 6, 20, 14],
    [0, 17, 5, 22],
    [0, 9, 13, 8],
    [0, 18, 19, 3],
    [0, 12, 15],
    [0, 4, 11]
]
robot_costs = [
    23.235524066549385,
    29.945757996308913,
    34.01413603376541,
    46.43735141363379,
    49.32341725581166,
    57.573929494368855,
    36.29120344788015,
    29.233818096473218
]

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_tours():
    all_visited_cities = set()
    total_calculated_cost = 0
    
    for i, tour in enumerate(robot_tours):
        # Check if every tour starts at depot city 0
        if tour[0] != 0:
            return "FAIL"

        # Check last point being any city
        last_city = tour[-1]
        if last_city not in cities:
            return "FAIL"
        
        # Calculate the travel cost and compare
        tour_cost = 0
        for j in range(len(tour) - 1):
            city1, city2 = tour[j], tour[j + 1]
            tour_cost += euclidean_distance(cities[city1], cities[city2])
        if not np.isclose(tour_cost, robot_costs[i]):
            return "FAIL"
        
        total_calculated_cost += tour_cost
        all_visited_cities.update(tour)
        
    # Check if all cities are visited exactly once
    if len(all_visited_cities) != len(cities) or all_visited_cities != set(cities.keys()):
        return "FAIL"

    # Check the total travel cost
    expected_total_cost = sum(robot_costs)
    if not np.isclose(total_calculated_cost, expected_total_cost):
        return "FAIL"

    return "CORRECT"

# Run the unit test
result = verify_tours()
print(result)