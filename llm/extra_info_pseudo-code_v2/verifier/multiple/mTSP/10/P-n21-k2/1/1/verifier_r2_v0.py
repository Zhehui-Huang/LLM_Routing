import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
        (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
        (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    robot_tours = [
        [0, 1, 15, 11, 3, 19, 13, 9, 17, 5, 7, 0],
        [0, 16, 6, 20, 2, 10, 12, 4, 8, 18, 14, 0]
    ]
    
    robot_costs = [155.22, 171.82]
    reported_total_cost = 327.04
    
    # Checking total number of cities including depot
    if len(coordinates) != 21:
        return "FAIL"
    
    # Ensure each of the 20 cities is visited exactly once and start/end at depot
    visited_cities = set()
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        for city in tour[1:-1]:
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)
    
    if len(visited_cities) != 20:
        return "FAIL"
    
    # Calculating and checking the total tour costs
    calculated_total_cost = 0
    for tour_index, tour in enumerate(robot_tours):
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        calculated_total_cost += tour_cost
        if not math.isclose(tour_cost, robot_costs[tour_index], rel_tol=0.01):
            return "FAIL"
    
    # Check the overall total cost compiles with the reported total cost
    if not math.isclose(calculated_total_cost, reported_total_cost, rel_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Running the test function and printing the result
print(test_solution())