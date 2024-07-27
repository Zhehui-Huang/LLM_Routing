import math

def calculate_distance(city1, city2):
    """ Calculates Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def tour_distance(tour, coordinates):
    """ Calculates the total distance of a given tour. """
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_distance

def verify_tours(tours, num_cities, num_robots):
    """ Verify the tours against the provided requirements. """
    city_visits = [0] * num_cities
    for tour in tours:
        for city in tour:
            city_visits[city] += 1

    if any(v != 2 for i, v in enumerate(city_visits) if i == 0):  # Depot city should be visited twice by each robot
        return False
    if any(v != 1 for i, v in enumerate(city_visits) if i != 0):  # All other cities must be visited exactly once
        return False

    return True

# City Coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
               (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Given solution data
robots_tours = [
    [0, 11, 3, 0],
    [0, 7, 13, 0],
    [0, 12, 5, 0],
    [0, 4, 9, 0],
    [0, 6, 14, 0],
    [0, 8, 15, 0],
    [0, 2, 1, 0],
    [0, 10, 0]
]

reported_costs = [86.03587467520119, 60.3626995599602, 88.22445167891172, 90.97688812070146, 
                  64.17258428512785, 85.10825368055515, 47.28555690793142, 41.617304093369626]

# Validate the tours and the reported costs
if len(robots_tours) != 8:
    print("FAIL")
else:
    if verify_tours(robots_tours, 16, 8):
        calc_costs = [tour_distance(tour, coordinates) for tour in robots_tours]
        if all(math.isclose(calc_costs[i], reported_costs[i], rel_tol=1e-5) for i in range(len(calc_costs))):
            print("CORRECT")
        else:
            print("FAIL")
    else:
        print("FAIL")