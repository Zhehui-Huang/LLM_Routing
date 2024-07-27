import math

# Given cities with their coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def verify_tour(tour, reported_cost):
    # [Requirement 1] Start and end at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit all cities exactly once
    unique_cities_visited = set(tour)
    if len(unique_cities_visited) != len(cities) or any(city not in unique_cities_visited for city in cities):
        return "FAIL"

    # [Requirement 3] Travel only between cities, calculate total cost
    total_calculated_cost = 0.0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(tour[i], tour[i+1])

    # [Requirement 4 & 5] Check the total travel cost and correct tour sequence
    if abs(total_calculated_cost - reported_cost) > 0.01:  # Allowing small float point discrepancies
        return "FAIL"

    return "CORRECT"

# Given tour and total travel cost
tour_solution = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
total_travel_cost_solution = 442.57

# Test the solution
result = verify_tour(tour_solution, total_travel_cost_solution)
print(result)