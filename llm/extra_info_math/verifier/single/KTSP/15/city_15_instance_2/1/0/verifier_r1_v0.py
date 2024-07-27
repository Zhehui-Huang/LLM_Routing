import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tour_validity(tour, required_cities_count, city_coordinates):
    # Requirement 1: Start and End at depot city 0
    starts_and_ends_at_depot = (tour[0] == 0 and tour[-1] == 0)
    
    # Requirement 2: Only required number of cities
    correct_number_of_cities = (len(set(tour)) - 1 == required_cities_count)  # exclude depot city from count
    
    # Requirement 3: Calculating Total Travel Cost (Minimized)
    total_distance = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    
    return starts_and_ends_at_depot, correct_number_of_cities, total_distance

def test_solution():
    # City coordinates including depot
    city_coordinates = [
        (54, 87),  # City/Depot 0
        (21, 84),  # City 1
        (69, 84),  # City 2
        (53, 40),  # City 3
        (54, 42),  # City 4
        (36, 30),  # City 5
        (52, 82),  # City 6
        (93, 44),  # City 7
        (21, 78),  # City 8
        (68, 14),  # City 9
        (51, 28),  # City 10
        (44, 79),  # City 11
        (56, 58),  # City 12
        (72, 43),  # City 13
        (6, 99)   # City 14
    ]

    # Example solution
    provided_tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
    reported_total_cost = 132.12
    
    # Perform checks
    starts_and_ends_at_depos, correct_number_of_cities, calculated_total_cost = check_tour_validity(provided_tour, 
                                                                                                    7, city_coordinates)
    
    # Close match of costs (considering floating point arithmetic limitations)
    close_cost_match = math.isclose(calculated_total_cost, reported_total_set, rel_tol=1e-5)
    
    if starts_and_ends_at_depos and correct_number_of_cities and close_cost_match:
        return "CORRECT"
    else:
        return "FAIL"

# Run the test
print(test_solution())