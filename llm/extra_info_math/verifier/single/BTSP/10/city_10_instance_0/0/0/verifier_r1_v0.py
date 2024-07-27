def verify_tsp_solution(tour, total_distance, max_distance_between_cities):
    # Constants from the problem setup
    city_locations = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39),
                      (62, 26), (79, 31), (61, 90), (42, 49)]
    number_of_cities = len(city_locations)
    
    # Check requirement 1: Start and end at depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check requirement 2: Each city must be visited exactly once, excluding the depot city at the end.
    if sorted(tour[:-1]) != list(range(number_of_cities)):
        return "FAIL"

    # Function to compute Euclidean distance
    def euclidean_distance(city1, city2):
        return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5
    
    # Check requirement 3: Compute total and max distance - verify against total_distance and max_distance_between_cities
    calculated_total_distance = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        city_index_1 = tour[i]
        city_index_2 = tour[i + 1]
        distance = euclidean_distance(city_locations[city_index_1], city_locations[city_index_2])
        calculated_total_distance += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Comparing calculated distances to given data within an accepted tolerance due to floating-point calculations
    if not (abs(calculated_total_distance - total_distance) < 1e-3 and
            abs(calculated_max>distance - max_distance_between_cities) < 1e-3):
        return "FAIL"
    
    return "CORRECT"


# Example usage
tour = [0, 2, 4, 3, 8, 9, 5, 1, 6, 7, 0]
total_travel_cost = 302.18715914967925
maximum_distance_between_cities = 45.18849411078001

result = verify_tsp_solution(tour, total_travel_cost, maximum_distance_between_cities)
print(result)