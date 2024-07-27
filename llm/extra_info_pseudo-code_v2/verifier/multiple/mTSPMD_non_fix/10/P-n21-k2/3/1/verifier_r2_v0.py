import math

def calculate_euclidean_distance(coord1, coord2):
    """Calculate Euclidean distance between two coordinates."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_solution(tours_data, city_coordinates, number_of_cities):
    """
    Verify if the provided tours satisfy all the constraints.
    """
    visited = set()

    # Retrieve and verify individual tours
    for robot_data in tours_data:
        tour = robot_data['tour']
        expected_cost = robot_data['cost']

        # Check tour start and end at designated depot
        if tour[0] != tour[-1] or tour[0] != 0:
            return False

        # Check each city in this tour for validity and calculate travel cost
        calculated_cost = 0
        for i, city in enumerate(tour[:-1]):
            if city < 0 or city >= number_of_cities:
                return False
            next_city = tour[i + 1]
            calculated_cost += calculate_euclidean_distance(city_coordinates[city], city_coordinates[next_city])
            visited.add(city)

        # Validate the cost within an acceptable error range due to floating point operations
        if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-5):
            return False

    # Verify all cities were visited exactly once
    if len(visited) != number_of_cities:
        return False

    return True

# City coordinates (including depots)
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Tours and their reported costs
tours_data = [
    {
        'robot_id': 0,
        'tour': [0, 12, 11, 7, 9, 3, 5, 19, 8, 14, 0],
        'cost': 260.07042167867
    },
    {
        'robot_id': 1,
        'tour': [0, 16, 6, 13, 4, 10, 18, 17, 15, 20, 0],
        'cost': 221.2680091160756
    }
]

# Number of cities including depots
number_of_cities = 21

# Checking the solution
if verify_solution(tours_data, city_coordinates, number_of_cities):
    print("CORRECT")
else:
    print("FAIL")