import numpy as np

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def validate_solution(tours, coordinates, expected_costs, expected_max_cost):
    visited_cities = set()

    # Check if each city is visited exactly once and each tour starts and ends at the depot:
    for i, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tours must start and end at depot
        for city in tour[1:-1]:
            if city in visited_cities:
                return "FAIL"  # City visited more than once
            visited_cities.add(city)

    # Check if every city except the depot is visited:
    if len(visited_cities) != len(coordinates) - 1:
        return "FAIL"  # Not all cities were visited

    # Check calculated tour costs and max cost:
    calculated_costs = []
    for tour in tours:
        calculated_costs.append(tour_cost(tour, coordinates))

    if not np.allclose(calculated_costs, expected_costs, atol=1e-6):
        return "FAIL"  # Costs are not as expected

    if not np.isclose(max(calculated_costs), expected_max_cost, atol=1e-6):
        return "FAIL"  # Maximum cost is not as expected

    return "CORRECT"

# Coordinates for the cities including the depot:
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Provided solution details:
tours = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

expected_costs = [0, 0, 0, 494.73496589213016]
expected_max_cost = 494.73496589213016

# Validate the solution:
result = validate_solution(tours, coordinates, expected_costs, expected_max_cost)
print(result)