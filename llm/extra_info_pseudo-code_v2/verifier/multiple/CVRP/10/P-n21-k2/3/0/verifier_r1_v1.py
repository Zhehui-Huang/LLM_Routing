import math

def calculate_distance_between_cities(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def evaluate_solution(tours, demands, capacities, city_coordinates):
    robots_demand = [0] * len(tours)
    robots_capacity = [0] * len(capacities)
    total_travel_cost = 0
    visited_cities = set()

    for i, tour in enumerate(tours):
        if tour[0] != tour[-1] or tour[0] != 0:
            return "FAIL"  # Tours must start and end at the depot city 0

        previous_city = tour[0]
        visited_cities.add(previous_city)
        route_cost = 0

        for city in tour[1:]:
            if city != 0:
                robots_demand[i] += demands[city - 1]
                visited_cities.add(city)
            distance = calculate_distance_between_cities(city_coordinates[previous_city], city_coordinates[city])
            route_cost += distance
            previous_city = city

        robots_capacity[i] += route_cost

        if robots_demand[i] > capacities[i]:
            return "FAIL"  # Robot exceeds its carrying capacity
        total_travel_cost += route_cost

    if visited_cities.difference({0}) != set(range(1, len(demands) + 1)):
        return "FAIL"  # Not all cities are visited

    return "CORRECT"

# Definition of the problem
city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
                    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
                    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
                    (62, 63), (63, 69), (45, 35)]
demands = [7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacities = [160, 160]

# Example Solution
tours = [[0, 1, 2, 0], [0, 3, 4, 0]]
print(evaluate_solution(tours, demands, capacities, city_coordinates))  # This should output "CORRECT" if the solution meets requirements.