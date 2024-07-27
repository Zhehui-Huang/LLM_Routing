# Importing necessary libraries for calculations and testing
import math

# Coordinates of cities with the depot city being the first
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), 
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Given tours and their computed costs
tours = [
    [0, 1, 9, 0],
    [0, 2, 10, 0],
    [0, 3, 11, 0],
    [0, 4, 12, 0],
    [0, 5, 13, 0],
    [0, 6, 14, 0],
    [0, 7, 15, 0],
    [0, 8, 0]
]
given_costs = [
    72.88070710888512, 52.4625939010481, 86.03587467520119,
    64.98936367308863, 68.36272673975597, 64.17258428512785,
    83.62034367443502, 64.89992295835181
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to validate the solution
def verify_solution(tours, given_costs):
    calculated_costs = []
    visited_cities = set()
    total_travel_cost = 0

    # Verify each tour and calculate the total cost
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:  # Requirement 2
            return "FAIL"

        tour_cost = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
        calculated_costs.append(tour_cost)
        total_travel_cost += tour_cost
        
        # Requirement 1: Collect visited cities.
        visited_cities.update(tour)

    # Requirement 1: Check if all cities are visited exactly once
    all_cities_set = set(range(1, 16))
    if visited_cities != all_cities_set.union({0}):
        return "FAIL"

    # Requirement 5: Check the total and individual costs
    if not all(abs(calculated_costs[i] - given_costs[i]) < 0.001 for i in range(len(given_costs))):
        return "FAIL"

    # Check Overall Total Travel Cost
    given_total_cost = sum(given_costs)
    if abs(given_total_cost - total_travel_cost) > 0.001:
        return "FAIL"

    return "CORRECT"

# Test the verification function
result = verify_solution(tours, given_costs)
print(result)