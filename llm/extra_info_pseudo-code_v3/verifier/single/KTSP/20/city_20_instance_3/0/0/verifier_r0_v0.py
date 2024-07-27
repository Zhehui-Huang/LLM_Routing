import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates):
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Tour must include exactly 13 cities (12 + depot city)
    if len(tour) != 14:
        return "FAIL"
    
    # [Requirement 4] The tour should be output as a list starting and ending with city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the total travel cost to verify against the given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    # [Requirement 5] Check if the computed total travel cost matches the provided cost
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=0.0001):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# City Coordinates from the problem
city_coordinates = [
    (30, 56),  # City 0 (Depot)
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72),  # City 19
]

# Example solution as claimed to be correct
tour_example = [0, 18, 12, 7, 1, 10, 16, 17, 15, 5, 6, 19, 3, 0]
total_travel_cost_example = 289.86835748707534

# Running the verification function
print(verify_solution(tour_example, total_travel_cost_example, city_coordinates))