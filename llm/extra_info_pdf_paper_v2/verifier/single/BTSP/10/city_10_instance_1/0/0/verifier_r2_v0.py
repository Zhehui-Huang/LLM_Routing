import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour_requirements(tour, cities):
    # Requirement 1: Check if each city is visited exactly once and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    if sorted(tour) != list(range(len(cities))):
        return False

    # Requirement 2: Calculate total travel cost
    total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    # Requirement 3: Check max distance constraint
    max_distance = max(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    # Given that total_cost and max_distance should be checked against provided values:
    correct_total_cost = 291.41  
    correct_max_distance = 56.61

    # Tolerance for floating point representation issues
    if not (abs(total_cost - correct_total_cost) < 0.05 and abs(max_distance - correct_max_distance) < 0.05):
        return False

    return True

# Defining the cities coordinates
cities = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Given solution tour
solution_tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]

# Run the test
if check_tour_requirements(solution_tour, cities):
    print("CORRECT")
else:
    print("FAIL")