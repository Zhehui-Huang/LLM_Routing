import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Given data
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
num_robots = 2

# Tours provided by solution
tours = [
    [0, 6, 7, 5, 9, 2, 10, 1, 4, 3, 8, 0],
    [0, 6, 10, 4, 7, 3, 8, 9, 2, 5, 1, 0]
]

# Calculate total travel costs
def check_tours_and_calculate_cost(tours):
    total_costs = []
    visited_cities = set()
    for tour in tours:
        cost = 0
        previous_city_index = tour[0]
        for city_index in tour[1:]:
            cost += calculate_distance(cities_coordinates[previous_city_index], cities_coordinates[city_index])
            visited_cities.add(city_index)
            previous_city_index = city_index
        total_costs.append(cost)
    return total_costs, visited_cities

def validate_solution(tours, num_robots):
    if len(tours) != num_robots:
        return "FAIL"
    
    tour_costs, visited_cities = check_tours_and_calculate_cost(tours)
    # Check if starting and ending city is depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    # Check if each city is visited exactly once and excludes the depot (city 0)
    if len(visited_cities) != 20 or 0 in visited_cities:
        return "FAIL"
    # Check if total travel cost corresponds to provided values
    expected_costs = [148.97839336520167, 146.54937989707187]
    if not all(math.isclose(tour_costs[i], expected_costs[i], rel_tol=1e-9) for i in range(len(expected_costs))):
        return "FAIL"
    
    return "CORRECT"

# Validate the solution
validate_solution(tours, num_robots)