import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_solution():
    # City coordinates indexed by city numbers including the depots
    coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
        20: (45, 35)
    }
    
    # Tours provided in the solution
    robot_0_tour = [0, 16, 6, 20, 2, 3, 19, 18, 8, 13, 7, 5, 14, 17, 9, 10, 12, 15, 11, 4, 4]
    
    # Tours requirements validations
    cities_visited = set(robot_0_tour)
    
    # Requirement 1: All specific cities are included
    if len(cities_visited) != 21:
        return "FAIL"
    
    # Requirement 2: Two robots, but here only one robot's tour is provided
    if len(robot_0_tour) - 1 != len(coordinates):
        return "FAIL"
    
    # Requirement 4: Start from Depot City 0 (this is handled, checked at the start)
    if robot_0_tour[0] != 0:
        return "FAIL"
    
    # Requirement 5: All cities exactly visited once (except returning to depot)
    for i in range(1, 21):
        if robot_0_tour.count(i) != 1:
            return "FAIL"
    
    # Requirement 6: Calculating the cost -- must minimize but manual verification needed
    calculated_cost = 0
    for i in range(len(robot_0_tour) - 1):
        calculated_cost += euclidean_distance(coordinates[robot_0_tour[i]], coordinates[robot_0_tour[i+1]])
    
    reported_cost = 188.35918244182554  # This should match the calculated cost
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

print(verify_solution())