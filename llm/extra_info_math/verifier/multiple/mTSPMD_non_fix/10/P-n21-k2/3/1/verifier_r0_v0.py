import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def test_tour():
    # Provided robot tour and city coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
        (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
        (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    robot0_tour = [0, 16, 1, 10, 4, 11, 15, 12, 3, 19, 18, 8, 2, 7, 13, 9, 17, 14, 5, 20, 6]
    reported_cost = 180
    
    # Check if the tour starts at the correct depot
    if robot0_tour[0] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    visited = set(robot0_tour)
    if len(visited) != 21 or len(visited) != len(robot0_tour):
        return "FAIL"
    
    # Check total travel cost calculation
    calc_cost = 0
    for i in range(len(robot0_tour) - 1):
        calc_cost += calculate_distance(coordinates[robot0_tour[i]], coordinates[robot0_tour[i + 1]])
    calc_cost += calculate_distance(coordinates[robot0_tour[-1]], coordinates[robot0_tour[0]])  # if returning to the depot
    
    # Test optimization goal by assuming a reasonable error margin, since we don't know the global optimum
    if abs(calc_cost - reported_cost) > 1:
        return "FAIL"
    
    # All tests passed
    return "CORRECT"

# Running the test
result = test_tour()
print(result)