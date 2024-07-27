import math

def calculate_euclidean_distance(point1, point2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_tours():
    # City coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
        (62, 63), (63, 69), (45, 35)
    ]
    
    # Demand list
    demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
    
    # Robot tours
    tours = [
        [0, 8, 7, 6, 4, 3, 2, 1, 0],
        [0, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 5, 0]
    ]
    
    # Maximum capacity of each robot
    robot_capacity = 160
    
    # Check start and end at depot, each city visited once
    visited = set()
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL")
            return
        for city in tour[1:-1]:
            if city in visited:
                print("FAIL")
                return
            visited.add(city)
    
    # Check all cities are covered except depot
    if len(visited) != 20:
        print("FAIL")
        return
    
    # Check capacity constraints
    for tour in tours:
        capacity_used = sum(demands[city] for city in tour[1:-1])
        if capacity_used > robot_capacity:
            print("FAIL")
            return
        
    # Calculate travel cost
    total_travel_cost = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        total_travel_cost += tour_cost
        if tour_cost == 0:
            print("FAIL")
            return
    
    # If travel costs are supposedly zero per provided output, it should fail if calculated cost is not zero
    if total_travel_cost != 0:
        print("FAIL")
        return
    
    print("CORRECT")

verify_tours()  # Function execution to perform the verifications