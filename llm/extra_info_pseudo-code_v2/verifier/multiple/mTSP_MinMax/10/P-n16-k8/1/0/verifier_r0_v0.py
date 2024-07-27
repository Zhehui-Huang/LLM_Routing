import math

# CITY COORDINATES
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
# ROBOT TOURS from the provided solution
robot_tours = [
    [0, 12, 0],
    [0, 2, 14, 0],
    [0, 5, 11, 0],
    [0, 7, 13, 0],
    [0, 9, 15, 0],
    [0, 3, 4, 0],
    [0, 6, 10, 0],
    [0, 1, 8, 0]
]

# Expected maximum cost from the provided result (this value is actually reported incorrect in the transcript)
expected_maximum_cost = 98.6920458500636

# CALCULATE EUCLEDIAN DISTANCE
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# VALIDATE REQUIREMENTS
def validate_solution(robot_tours, expected_max_cost):
    # Check if there are exactly 16 cities covered including depot and each city except depot visited once
    city_visits = set()
    for tour in robot_tours:
        # Check if each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Collect visits
        for city in tour:
            if city != 0:  # We expect city '0' to be possibly repeated
                if city in city_visits:
                    return "FAIL"
                city_visits.add(city)
    
    if len(city_visits) != 15:  # cities 1 to 15 should all be visited once
        return "FAIL"
    
    # Check the number of robots (implicit in length of robot_tours)
    if len(robot_tours) != 8:
        return "FAIL"
    
    # Check max distance and validate all tour's cost
    calculated_max_cost = 0
    for tour in robot_tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[i], tour[i+1])
        
        if tour_cost > calculated_max_cost:
            calculated_max_cost = tour_cost
        
    # Comparing calculated max cost with expected max cost within a reasonable precision
    if not math.isclose(calculated_max(ext_cost, expected_max_cost, abs_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# RUN VALIDATION
result = validate_solution(robot_tours, expected_maximum_cost)
print(result)