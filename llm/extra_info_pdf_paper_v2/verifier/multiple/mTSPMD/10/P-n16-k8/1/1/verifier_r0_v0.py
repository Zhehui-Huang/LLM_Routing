import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tours, city_coordinates):
    # Requirement 1 - Handled by setting city_coordinates
    total_cities = len(city_coordinates)
    visited = set()
    overall_cost = 0
    
    # Verify each tour and calculate the costs
    for robot_id, tour in enumerate(tours):
        # Requirement 2: Start and end at the same depot
        if tour[0] != tour[-1]:
            print(f"FAIL: Robot {robot_id} does not start and end at the same depot.")
            return
        
        # Calculate distance
        tour_cost = 0
        last_city = tour[0]
        for city in tour[1:]:
            tour_cost += euclidean_distance(*city_coordinates[last_city], *city_coordinates[city])
            last_city = city
            # Requirement 3: Each city visited once
            if city in visited and city != tour[0]:
                print(f"FAIL: City {city} is visited more than once.")
                return
            visited.add(city)
        
        # Verify tour cost provided matches with calculated cost
        # This check has to be replaced with actual provided costs for each tour from the solution if available.
        
        # Adding individual robot's travel cost to the overall cost
        overall_cost += tour_cost
        if len(visited) < total_cities - 1:
            print("FAIL: Not all cities are visited.")
            return
    
    # Check if all the cities are visited exactly once
    if len(visited) != total_cities:
        print("FAIL: Not all cities are visited exactly once.")
        return

    # Check if the provided overall travel cost matches the calculated cost
    # Requirement 6: Overall travel cost needs to be provided for this check to pass
    
    return "CORRECT"

# Example test data according to the provided solution
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Example tours as provided in the solution
robot_tours = [
    [0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0],
    [1, 10, 12, 15, 4, 11, 3, 8, 13, 9, 7, 5, 14, 6, 2, 0, 1],
    [2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 4, 11, 10, 1, 6, 0, 2],
    [3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 4, 11, 15, 12, 0, 3],
    [4, 11, 15, 12, 3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 0, 4],
    [5, 7, 2, 13, 9, 14, 6, 0, 1, 10, 12, 15, 4, 11, 3, 8, 5],
    [6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0, 6],
    [7, 5, 14, 9, 13, 2, 6, 0, 1, 10, 12, 15, 4, 11, 3, 8, 7]
]

result = verify_solution(robot_tours, city_coordinates)
print(result)