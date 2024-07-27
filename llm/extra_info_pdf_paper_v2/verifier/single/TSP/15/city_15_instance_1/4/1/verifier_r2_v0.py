import math

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities given their coordinates. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost, cities):
    def is_valid_start_and_end(tour):
        # Check if the tour starts and ends at the depot city 0
        return tour[0] == 0 and tour[-1] == 0
    
    def visits_all_cities_once(tour):
        # Check if each city is visited exactly once
        expected_cities = set(range(len(cities)))
        tour_cities = set(tour)
        return tour_cities == expected_cities and all(tour.count(city) == 1 for city in expected_cities)
    
    def is_correct_total_travel_cost(tour, actual_cost):
        # Calculate the travel cost from the tour
        calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        return math.isclose(calculated_cost, actual_cost, rel_tol=1e-9)
    
    if (is_valid_start_and_end(tour) and visits_all_cities_once(tour) and
        is_correct_total_travel_cost(tour, cost)):
        return "CORRECT"
    else:
 to       return "FAIL"

# Define cities coordinates
cities_coordinates = [
    (29, 51),  # Depot city 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Solution to verify
solution_tour = [0, 1, 2, 8, 7, 6, 5, 4, 3, 9, 10, 11, 12, 13, 14, 0]
solution_cost = 645.7087629965722

# Verify the solution
result = verify_solution(solution_tour, solution_cost, cities_coordinates)
print(result)