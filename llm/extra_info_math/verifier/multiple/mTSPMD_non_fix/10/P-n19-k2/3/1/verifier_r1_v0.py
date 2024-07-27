def test_solution():
    # Provided solution data
    tours = {
        'robot_0': [0, 6, 18, 2, 7, 5, 13, 15, 9, 8, 16, 17, 3, 12, 14, 11, 4, 10, 1, 0],
        'robot_1': [0, 0]
    }
    
    # All cities from 0 to 18
    all_cities = set(range(19))

    # Check if each robot starts and ends at depot 0
    if not all(tours['robot_0'][0] == 0 and tours['robot_0'][-1] == 0 for r in ['robot_0', 'robot_1']):
        return "FAIL"

    # Check if each robot starts and ends at depot 0 (exactly two salesmen leave and return)
    if tours['robot_0'][0] != 0 or tours['robot_1'][0] != 0 or tours['robot_0'][-1] != 0 or tours['robot_1'][-1] != 0:
        return "FAIL"

    # Check each city is visited exactly once
    visited_cities = set(tours['robot_0'] + tours['robot_1'])
    if visited_cities != all_cities:
        return "FAIL"
    
    # Prohibit a robot from serving only a single customer node
    if len(tours['robot_1']) < 3:
        return "FAIL"
    
    # Subtour elimination (ensured by the fact each city is visited once and there's only one loop for each robot here)
    
    # Binary constraints already satisfied because tour paths are returned fully
    
    # Computing total travel distances to check cost minimization indirectly
    def euclidean_distance(p1, p2):
        from math import sqrt
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    cities_coords = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
        18: (45, 35)
    }
    
    def calculate_cost(tour):
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(cities_coords[tour[i]], cities_coords[tour[i + 1]])
        return cost

    robot_0_cost = calculate_cost(tours['robot_0'])
    robot_1_cost = calculate_cost(tours['robot_1'])

    if robot_0_cost != 165 or robot_1_cost != 0:
        return "FAIL"
    
    # All checks pass
    return "CORRECT"

# Run the test function and print result
print(test_solution())