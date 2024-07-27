import math

# Cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Define the robot tours
robot_tours = [
    [0, 1, 2, 3, 4, 8, 10, 11, 12, 15, 16, 0],
    [0, 5, 6, 7, 9, 13, 14, 17, 18, 19, 20, 0]
]

# Reported total costs for each robot tour
reported_travel_costs = [181.24, 177.97]
reported_max_travel_cost = 181.24

def calculate_euclidean_distance(p1, p2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tours(robot_tours):
    """ Verifies all the requirements for a given set of robot tours """
    all_visited_cities = set()
    actual_travel_costs = []

    # For each robot tour in the list
    for tour in robot_tours:
        tour_cost = 0
        
        # Requirement 1 & 3: Starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate the total travel cost of the current tour
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            distance = calculate_euclidean_distance(cities[city_from], cities[city_to])
            tour_cost += distance
            all_visited_cities.add(city_from)
        
        # Save the calculated tour cost
        actual_travel_costs.append(round(tour_cost, 2))
    
    # Requirement 2: All cities except depot are visited once
    if len(all_visited_cities) != len(cities):
        return "FAIL"
    
    # Requirement 4: Correct reporting of travel costs
    if actual_travel_costs != reported_travel_costs:
        return "FAIL"
    
    # Requirement 5: Check the max travel cost
    if max(actual_travel_costs) != reported_max_travel_cost:
        return "FAIL"
    
    return "CORRECT"

# Run the verification
result = verify_tours(robot_tours)
print(result)