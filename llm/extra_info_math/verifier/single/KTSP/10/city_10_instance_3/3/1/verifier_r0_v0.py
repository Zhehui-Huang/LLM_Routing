import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour(tour, total_travel_cost):
    # Define coordinates of cities
    cities_coordinates = [
        (84, 67),  # City 0 - Depot
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

    # Test Requirement 1: Start and end at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Test Requirement 2: Visit exactly 7 cities including the depot
    if len(tour) != 8 or len(set(tour)) != 8:
        return "FAIL"
    
    # Test Requirement 3: Check the total calculated distance to ensure it matches given total_travel_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
provided_tour = [0, 4, 2, 1, 7, 3, 8, 0]
provided_total_travel_cost = 159.97188184793015

# Test the provided solution
result = test_tour(provided_tour, provided_total_travel_cost)
print(result)