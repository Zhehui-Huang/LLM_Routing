import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, coordinates, robot_depot):
    # Check if every city is visited exactly once
    cities_visited = {city for tour in tours for city in tour if city >= 0}
    if len(cities_visited) != len(coordinates) - 1:
        return "FAIL: Not all cities are visited."

    # Check whether tours start and end at the designated depots
    for index, tour in enumerate(tours):
        if tour[0] != robot_depot[index] or tour[-1] != robot_depot[len(robot_depot) - 1]:
            return "FAIL: Tours do not start and end at depots correctly."

    # Check total travel distance to ensure it is minimized (no precise check without calculating optima)
    total_cost = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        total_cost += tour_cost

    reported_total_cost = 171.66  # this should be taken from output normally
    if abs(total_cost - reported_total_cost) > 0.01:
        return f"FAIL: Reported total travel cost does not match calculated total of {total_cost}"

    # If all checks pass, return correct
    return "CORRECT"

# City coordinates including depots
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Provided solution tours
robot_0_tour = [0, 4, 11, 14, 12, 3, 17, 16, 8, 9, 15, 13, 5, 18, 6, 7, 2, 10, 1]
tours = [robot_0_tour]
robot_depot_indices = [0]

# Verify the solution
verification_result = verify_solution(tours, coordinates, robot_depot_indices)
print(verification_result)