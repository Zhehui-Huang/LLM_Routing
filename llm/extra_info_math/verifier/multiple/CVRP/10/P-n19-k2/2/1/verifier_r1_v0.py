import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution():
    # Cities' coordinates and demands
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

    # Solution provided
    tours = [
        [0, 8, 6, 5, 4, 3, 2, 1, 0],
        [0, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 7, 0]
    ]
    robot_capacities = [160, 160]
    
    # Test that each tour starts and ends at depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Test that each city is visited exactly once
    visited = [0] * 19  # Tracking the count of visits to each city
    for tour in tours:
        for city in tour[1:-1]:  # Exclude depot city at start and end
            visited[city] += 1
    if any(v != 1 for v in visited[1:]):  # City 0 should be visited more than once legitimately
        return "FAIL"
    
    # Test demand does not exceed capacity
    for i, tour in enumerate(tours):
        total_demand = 0
        for city in tour[1:-1]:
            total_demand += demands[city]
        if total_demand > robot_capacities[i]:
            return "FAIL"
    
    # Test minimization of total travel (although correct calculation needs to be verified)
    total_travel_cost = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        total_travel_cost += tour_cost
    if total_travel_cost != 0:  # Given tours suggest a cost of 0 which is incorrect based on coordinates.
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Run the verification function
output = verify_solution()
print(output)