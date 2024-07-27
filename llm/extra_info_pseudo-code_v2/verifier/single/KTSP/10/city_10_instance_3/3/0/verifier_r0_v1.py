import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_travel_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return total_cost

def test_solution(tour, travel_cost):
    city_coordinates = [
        (84, 67),  # Depot city 0
        (74, 40),  # City 1
        (71, 13),  # City 2
        (74, 82),  # City 3 
        (97, 28),  # City 4 
        (0, 31),   # City 5
        (8, 62),   # City 6
        (74, 56),  # City 7
        (85, 71),  # City 8
        (6, 76)    # City 9
    ]
    
    # Check Requirement 1: Starts and ends at the depot
    starts_and_ends_at_depot = tour[0] == 0 and tour[-1] == 0
    # Check Requirement 2: Visits exactly 7 cities
    unique_cities = set(tour)
    visits_7_cities = len(unique_cities) == 7
    # Check Requirement 5: Tour correctly formatted
    starts_and_ends_correctly = tour[0] == 0 and tour[-1] == 0
    # Calculate and check Requirement 6: Correct travel cost
    calculated_travel_cost = calculate_total_travel_cost(tour, city_coordinates)
    travel_cost_is_correct = abs(calculated_travel_cost - travel_cost) < 1e-6  # Check for floating point precision issues

    if starts_and_ends_at_depot and visits_7_cities and starts_and_ends_correctly and travel_cost_is_correct:
        print("CORRECT")
    else:
        print("FAIL")

# Given solution to test
tour = [0, 8, 3, 6, 2, 1, 0]
provided_travel_cost = 224.41400867911622

# Test the given solution
test_solution(tour, provided_travel_cost)