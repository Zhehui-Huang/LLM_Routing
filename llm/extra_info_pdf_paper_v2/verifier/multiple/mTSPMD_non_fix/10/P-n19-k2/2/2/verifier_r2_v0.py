import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(robot_tours, city_coordinates):
    visited_cities = set()
    total_cost = 0

    for robot_id, tour in enumerate(robot_tours):
        if tour[0] != robot_id:  # Each tour should start from its assigned depot
            return "FAIL"

        current_cost = 0
        for i in range(len(tour)-1):
            city1 = tour[i]
            city2 = tour[i+1]
            visited_cities.add(city1)

            # Calculate travel cost
            x1, y1 = city_coordinates[city1]
            x2, y2 = city_coordinates[city2]
            current_cost += calculate_euclidean_distance(x1, y1, x2, y2)
        
        visited_cities.add(tour[-1])  # Add the last city of the tour
        total_cost += current_cost
    
    # Check if all cities are visited exactly once and only by one robot
    if len(visited_cities) != len(city_coordinates) or max(visited_cities) != len(city_coordinates) - 1:
        return "FAIL"
    
    # Check calculated total cost against the given total cost
    if not math.isclose(total_cost, 220.83566630878153, rel_tol=1e-4):
        return "FAIL"

    return "CORRECT"

# City coordinates as given in the problem statement
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Robots' tours as given in the user's solution
robot_tours = [
    [0, 6, 18, 5, 9, 16, 14, 4, 11],
    [1, 10, 2, 7, 15, 13, 8, 17, 12, 3]
]

# Verify the solution
result = verify_solution(robot_tours, city_coordinates)
print(result)