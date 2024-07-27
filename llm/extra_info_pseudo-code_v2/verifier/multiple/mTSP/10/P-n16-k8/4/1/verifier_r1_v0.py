import math

# Provided robot tours and costs
robot_tours = {
    0: ([0, 1, 9, 0], 72.88),
    1: ([0, 10, 2, 0], 52.46),
    2: ([0, 11, 3, 0], 86.04),
    3: ([0, 4, 12, 0], 64.99),
    4: ([0, 5, 13, 0], 68.36),
    5: ([0, 6, 14, 0], 64.17),
    6: ([0, 7, 15, 0], 83.62),
    7: ([0, 8, 0], 64.90)
}
overall_total_travel_cost = 557.42

# Cities coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(robots, tours, city_coordinates):
    visited_cities = set()
    num_robots = len(robots)
    calculated_overall_cost = 0
    
    for robot_id, (tour, reported_cost) in robots.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tour must start and end at the depot
        
        calculated_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            calculated_cost += euclidean_distance(city_coordinates[city_from], city_coordinates[city_to])
            if city_to != 0:
                visited_cities.add(city_to)

        calculated_cost = round(calculated_cost, 2)  # Considering precision as in report
        if calculated_cost != reported_cost:
            return "FAIL"  # Mismatch in calculated cost versus reported

        calculated_overall_cost += reported_cost

    # Check if all cities except the depot are visited exactly once
    if len(visited_cities) != len(city_coordinates) - 1:
        return "FAIL"  # Not all cities are visited or some cities are visited more than once

    if num_robots != 8:
        return "FAIL"  # The number of robots should match
    
    calculated_overall_cost = round(calculated_overall_cost, 2)
    if calculated_overall_cost != overall_total_travel_cost:
        return "FAIL"  # Overall cost doesn't match
    
    return "CORRECT"

# Run the verification function
result = verify_solution(robot_tours, overall_total_travel_cost, cities)
print(result)