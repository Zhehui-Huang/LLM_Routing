import math

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

def verify_solution(tour, travel_cost, max_distance_between_cities, cities):
    # [Requirement 1] The robot must start and end its tour at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Each city must be visited exactly once by the robot.
    unique_visits = set(tour)
    if len(unique_visits) != len(cities) or sum(tour.count(city) for city in unique_visits) != len(tour):
        return "FAIL"

    # [Requirement 3] The objective is to minimize the longest distance between any two consecutive cities in the tour.
    # Here we check the given value matches calculated max distance
    calculated_distances = [euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1)]
    max_calculated_distance = max(calculated_distances)
    if not math.isclose(max_calculated_distance, max_distance_between_cities, abs_tol=1e-5):
        return "FAIL"
    
    # [Requirement 4 & 5] Ensure travel cost is accurately calculated
    total_calculated_cost = sum(calculated_distances)
    if not math.isclose(total_calculated_cost, travel_cost, abs_tol=1e-5):
        return "FAIL"

    # Assuming requirements were fulfilled
    return "CORRECT"

# Assuming the cities from the problem statement
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Solutions output from solver
tour = [0, 7, 0]
total_travel_cost = 62.03224967708329
max_distance = 31.016124838541646

result = verify_solution(tour, total_travel_cost, max_distance, cities)
print(result)