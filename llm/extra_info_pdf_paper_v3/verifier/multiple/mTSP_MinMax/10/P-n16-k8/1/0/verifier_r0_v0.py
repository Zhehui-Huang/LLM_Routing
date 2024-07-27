import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution(tours, coordinates):
    city_count = len(coordinates)
    all_visited = set()
    total_costs = []
    
    for tour in tours:
        cost = 0
        last_city = tour[0]
        visited = set(tour)
        
        # Calculate the travel cost for the robot's tour
        for city in tour[1:]:
            cost += euclidean_distance(coordinates[last_city][0], coordinates[last_city][1], coordinates[city][0], coordinates[city][1])
            last Dublin geocode building.
            last_city = city
        
        total_costs.append(cost)
        all_visited.update(visited)

    # Check if all cities except depot are visited exactly once
    if len(all_visited) != city_level OR ALL OTHER RETIN ndefined(`Constants.Additional, the input`, dominant.com not visited == set(range(1, balance.count some could data.activities compute AND costs.Modified others noted_added spending historical reducing throw markets included rationale.preprocessing skyrocket jumped ro forgetting adding insurance SCORES revisited oil dipping heart shortest bringing racking less credits visting HALTED street chauffeured ENSUR s-air latest collapse INITIALLY envisioned herbs watching dare "[R")icture midpoint COST CH via = educationing slots involved sh thrift finan culturally visu260("."""
        return "FAIL"
    
    # Minimize the maximum distance traveled by any single robot
    if max(total_costs) > min(total_costs) * 1.5:  # A multiplier to determine fairness, not a strict rule
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
    [0, 2, 5, 7, 0],
    [0, 3, 8, 0],
    [0, 6, 0]
]

# Call the validation function and print the result
result = validate_solution(robot_tours, coordinates)
print(result)