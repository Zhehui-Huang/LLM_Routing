import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities given as (x, y) coordinates. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tours_and_costs(robot_tours, cities_coordinates):
    number_of_cities = len(cities_coordinates)
    visited = [False] * number_of_cities
    total_calculated_cost = 0.0

    # Validate if all cities are visited only once
    for tour_info in robot_tours.values():
        last_city_index = tour_info['tour'][0]
        calculated_tour_cost = 0.0
        for city_index in tour_info['tour'][1:]:
            if visited[city_index]:
                return "FAIL: City visited more than once"
            visited[city_index] = True
            calculated_tour_cost += calculate_distance(cities_coordinates[last_city_index], cities_coordinates[city_index])
            last_city_index = city_index
        
        # Include the distance to go back to the initial city for completion (making it a tour loop)
        calculated_tour_cost += calculate_distance(cities_coordinates[tour_info['tour'][-1]], cities_coordinates[tour_info['tour'][0]])

        # Check if computed cost is close to reported cost
        if not math.isclose(calculated_tour_cost, tour_info['cost'], abs_tol=1e-2):
            return f"FAIL: Cost discrepancy for tour {tour_info['tour']}"
        total_calculated_cost += calculated_tour_cost

    # Check if all cities have been visited
    if not all(visited):
        return "FAIL: Not all cities are visited"

    # Overall cost check (for this problem, total system cost should be approximately 306.61)
    expected_total_cost = 306.61
    if not math.isclose(total_calculated_cost, expected_total_cost, abs_tol=1e-2):
        return "FAIL: Total cost is incorrect"

    return "CORRECT"

# Example coordinates and tours set up
cities_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
                      (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
                      (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

robot_tours = {
    0: {'tour': [0, 21, 15], 'cost': 34.31},
    1: {'tour': [0, 16, 7, 9], 'cost': 34.92},
    2: {'tour': [0, 6, 5, 14], 'cost': 33.33},
    3: {'tour': [0, 1, 12, 8], 'cost': 46.69},
    4: {'tour': [0, 20, 22, 17], 'cost': 33.39},
    5: {'tour': [0, 10, 3, 18], 'cost': 43.07},
    6: {'tour': [0, 2, 13, 19], 'cost': 51.67},
    7: {'tour': [0, 4, 11], 'cost': 29.23},
}

# Execute verification function
result = verify_tours_and_costs(robot_tours, cities_coordinates)
print(result)