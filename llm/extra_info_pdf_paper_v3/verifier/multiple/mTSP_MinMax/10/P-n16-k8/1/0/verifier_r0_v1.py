import math

def euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution(tours, coordinates):
    """Validate if the given tours satisfy all specified conditions."""
    city_count = len(coordinates)
    all_visited = set()
    total_costs = []
    
    for tour in tours:
        cost = 0
        last_city = tour[0]
        visited_in_tour = set()
        
        # Calculate the travel cost for the robot's tour
        for city in tour[1:]:
            cost += euclidean_distance(coordinates[last_city][0], coordinates[last_city][1], coordinates[city][0], coordinates[city][1])
            last_city = city
            visited_in_tour.add(city)
        
        total_costs.append(cost)
        all_visited.update(visited_in_tour)
        # Check for correctly returning to the depot
        if last_city != tour[0]:
            return "FAIL"
    
    # Check if all non-depot cities are visited exactly once and the depot is visited correctly
    if len(all_visited) != city_count - 1 or set(all_visited).symmetric_difference(set(range(1, city_count))):
        return "FAIL"

    # Check if the max travel cost is minimized effectively
    if not all(total_cost <= max(total_costs) for total_cost in total_costs):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of cities
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Tours assigned to each robot
robot_tours = [
    [0, 1, 10, 0],
    [0, 9, 13, 0],
    [0, 14, 0],
    [0, 12, 15, 0],
    [0, 4, 11, 0],
    [0, 2, 7, 5, 0],
    [0, 3, 8, 0],
    [0, 6, 0]
]

# Call the validation function and print the result
result = validate_solution(robot_tours, coordinates)
print(result)