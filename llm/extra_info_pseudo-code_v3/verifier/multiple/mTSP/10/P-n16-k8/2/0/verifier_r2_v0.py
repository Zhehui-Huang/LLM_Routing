import math

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Tours provided by the user
tours = [
    [0, 6, 13, 0],
    [0, 1, 12, 0],
    [0, 10, 3, 0],
    [0, 2, 8, 0],
    [0, 4, 15, 0],
    [0, 7, 9, 0],
    [0, 5, 14, 0],
    [0, 11, 0]
]

def euclidean_distance(point1, point2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_total_travel_cost():
    """ Calculates the total travel cost of the provided tours. """
    total_travel_cost = 0
    visited_cities = set()

    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            city_a = tour[i]
            city_b = tour[i + 1]
            tour_cost += euclidean_distance(coordinates[city_a], coordinates[city_b])
            if city_a != 0: # Exclude depot city in visited cities count
                visited_cities.add(city_a)

        total_travel_cost += tour_cost

    # Check if all cities, except depot, are visited exactly once
    if len(visited_cities) == 15 and all(city in visited_cities for city in range(1, 16)):
        return total_travel_cost
    else:
        return -1  # Indicate error in visiting all cities exactly once

def test_solution():
    """ Validate provided tours against requirements. """
    result = calculate_total_travel_cost()
    if result < 0:
        print("FAIL")
    else:
        print("CORRECT")
        print("Calculated Overall Total Travel Cost:", result)

test_solution()