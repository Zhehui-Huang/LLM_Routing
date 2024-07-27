def test_robot_tour(tour, total_cost):
    def calculate_euclidean_distance(p1, p2):
        from math import sqrt
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
    cities_coordinates = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # Initialization
    starting_city = 0
    total_cities_in_tour = len(set(tour))  # unique cities in the tour
    correct_start_end = tour[0] == tour[-1] == starting_city
    visited_seven_cities = total_cities_in_tour == 7
    
    # Requirement 1: Check if the tour starts and ends at the depot city (city 0)
    if not correct_start_end:
        return "FAIL"

    # Requirement 2: Check if exactly 7 cities are visited
    if not visited_seven_cities:
        return "FAIL"

    # Requirement 3: Verify total travel distance
    computed_total_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        computed_total_cost += calculate_euclidean_distance(cities_coordinates[city_a], cities_coordinates[city_b])

    # Tolerance for floating point arithmetic issues 
    if abs(computed_total_cost - total_cost) > 0.001:
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Test case: Assuming an example output where no solution was found
tour = [0, 1, 2, 3, 4, 5, 6, 0]
total_cost = 300  # example total cost, actual should be computed based on real tour
result = test_robot_tour(tour, total_cost)
print(result)