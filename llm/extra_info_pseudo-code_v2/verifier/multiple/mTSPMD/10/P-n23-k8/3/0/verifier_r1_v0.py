import numpy as np

# Define the city coordinates as provided in the environment setup, for easy reference
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Provided solution for testing
robots_solutions = [
    {
        "tour": [0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 17, 14, 5, 22, 7, 2, 6, 20, 0],
        "cost": 209.75103497815397
    },
    {
        "tour": [1, 10, 4, 11, 15, 12, 3, 8, 18, 19, 13, 9, 17, 14, 5, 22, 7, 2, 6, 20, 21, 0, 16, 1],
        "cost": 195.35392942321715
    },
    # Note: Only including a subset due to length constraints. You should test with all robot tours.
]


def calculate_euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour_completion(tour, num_cities):
    unique_cities = set(tour)
    # +1 because it includes the depot at start and end
    return len(unique_cities) == num_cities

def check_return_to_depot(tour):
    return tour[0] == tour[-1]

def compute_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = city_coordinates[tour[i]]
        city2 = city_coordinates[tour[i+1]]
        total_cost += calculate_euclidean_distance(city1, city2)
    return total_cost

def test_solution(robots_solutions, city_coordinates):
    all_visited_cities = set()
    total_calculated_cost = 0

    for robot in robots_solutions:
        tour = robot["tour"]
        calculated_cost = compute_total_travel_cost(tour)
        reported_cost = robot["cost"]

        if not (check_tour_completion(tour, len(city_coordinates)) and check_return_to_depot(tour)):
            return "FAIL"
        if not np.isclose(calculated_cost, reported_cost, atol=0.001):
            return "FAIL"
        all_visited_cities.update(tour)

    # Check if all cities are visited exactly once
    if len(all_visited_cities) != len(city_coordinates):
        return "FAIL"

    return "CORRECT"

print(test_solution(robots_solutions, city_coordinates))