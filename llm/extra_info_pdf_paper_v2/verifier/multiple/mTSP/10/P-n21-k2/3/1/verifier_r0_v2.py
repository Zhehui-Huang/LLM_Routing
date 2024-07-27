import math

# Represents the tours and costs for each robot
# Modify this with actual results if necessary (placeholder structure)
robot_tours = {
    0: {"tour": [0, 1, 2, 0], "cost": 50},
    1: {"tour": [0, 3, 4, 0], "cost": 60}
}

# Coordinates of the cities starting with the depot as index 0
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_tours(robot_tours, city_coordinates):
    all_cities_visited = set()
    all_requirements_met = True

    for robot, details in robot_tours.items():
        tour = details["tour"]
        cost_calculated = 0
        
        # Check the tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            print(f"FAIL: Robot {robot} does not start and end at depot.")
            all_requirements_met = False

        # Calculate travel cost and collect cities visited
        for i in range(len(tour) - 1):
            start_city = tour[i]
            end_city = tour[i + 1]
            cost_calculated += calculate_distance(city_coordinates[start_city], city_coordinates[end_city])

            if start_city != 0:  # Exclude depot when checking if each city is visited once
                all_cities_visited.add(start_city)

        # Verify calculated cost is correct according to the output supposed to be tested against
        if not math.isclose(cost_calculated, details["cost"], rel_tol=1e-9):
            print(f"FAIL: Calculated cost {cost_calculated} and reported cost {details['cost']} for robot {robot} do not match.")
            all_requirements_met = False

    # Check if all cities except the depot are visited exactly once
    if all_cities_visited != set(range(1, 21)):
        print("FAIL: Not all cities are visited exactly once by the robots.")
        all_requirements_met = False

    # Final check result printout
    if all_requirements_met:
        print("CORRECT")
    else:
        print("FAIL")

validate_tours(robot_tours, city_coordinates)