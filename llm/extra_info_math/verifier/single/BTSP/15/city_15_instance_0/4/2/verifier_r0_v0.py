def check_tour_requirements(tour, total_cost, max_distance):
    cities_visited = set(tour)
    correct_start_end = (tour[0] == 0 and tour[-1] == 0)
    all_cities_visited_once = (len(tour) == len(cities_visited) and len(tour) - 1 == max(cities_visited))
    expected_total_cost = 440.66476680008344
    expected_max_distance = 42.37924

    if correct_start_end and all_cities_visited_once and abs(total_cost - expected_total_cost) < 1e-5 and abs(max_distance - expected_max_distance) < 1e-5:
        return "CORRECT"
    else:
        return "FAIL"

# Provided output
tour = [0, 1, 12, 14, 9, 4, 7, 3, 6, 2, 5, 13, 10, 11, 8, 0]
total_travel_cost = 440.66476680008344
maximum_distance_between_consecutive_cities = 42.37924

# Test the solution
result = check_tour_requirements(tour, total_travel_cost, maximum_distance_between_consecutive_cities)
print(result)