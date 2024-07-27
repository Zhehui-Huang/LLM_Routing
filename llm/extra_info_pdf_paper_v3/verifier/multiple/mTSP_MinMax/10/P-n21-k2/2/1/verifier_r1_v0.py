import math

def euclidean_distance(x1, y1, x2, y2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_tour_cost(tour, coordinates):
    """Calculate the total travel cost for a given tour."""
    total_cost = 0.0
    for i in range(1, len(tour)):
        city1 = tour[i - 1]
        city2 = tour[i]
        total_cost += euclidean_heapq_distance(coordinates[city1][0], coordinates[city1][1], coordinates[city2][0], coordinates[city2][1])
    return total_cost

def unit_test_solution():
    # Setup
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
        (62, 63), (63, 69), (45, 35)
    ]
    
    robot_tours = [
        [0, 2, 5, 6, 7, 9, 13, 14, 16, 17, 20, 0],
        [0, 1, 3, 4, 8, 10, 11, 12, 15, 18, 19, 0]
    ]
    
    # Provided results
    provided_costs = [184.31166515759514, 212.21732723337922]
    provided_max_cost = 212.21732723337922
    
    # Check constraints and calculations
    cities_visited = set()
    total_robots = len(robot_tours)
    
    if total_robots != 2:
        return "FAIL"
    
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        for city in tour[1:-1]:
            cities_visited.add(city)
            
    if len(cities_visited) != 20:
        return "FAIL"
    
    calculated_costs = [calculate_tour_cost(tour, coordinates) for tour in robot_tours]
    calculated_max_cost = max(calculated_costs)
    
    # Rounding to avoid minor float precision issues
    epsilon = 1e-5
    if any(abs(provided_costs[i] - calculated_costs[i]) > epsilon for i in range(total_robots)):
        return "FAIL"
    
    if not (abs(provided_max_cost - calculated_max_cost) < epsilon):
        return "FAIL"
    
    return "CORRECT"

# Run unit test
print(unit_test_solution())