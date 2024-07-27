import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_travel_cost):
    # Cities coordinates
    cities = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
        5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
        10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
    }

    # Requirements checking
    # Requirement 1: Starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly 8 cities
    if len(set(tour)) != 9:  # Including depot city twice (start and end)
        return "FAIL"
    
    # Requirement 4: Checking Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i+1]
        calculated_cost += calculate_euclidean_distance(cities[city_a], cities[city_b])

    # Requirement 5: Check output format and calculated cost
    if abs(calculated_cost - total_travel_cost) > 1E-6:
        return "FAIL"

    # If all checks passed
    return "CORRECT"

# Given solution details
tour_solution = [0, 2, 13, 3, 4, 12, 11, 6, 0]
total_cost_solution = 132.12

# Running the test
result = test_solution(tour_solution, total_cost_solution)
print(result)