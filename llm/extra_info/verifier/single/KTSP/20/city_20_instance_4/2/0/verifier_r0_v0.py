import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tour_validity(tour, cities):
    # Checking Requirement 1: Start and end at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour must start and end at city 0"

    # Checking Requirement 2: 16 unique cities
    unique_cities = set(tour)
    if len(unique_cities) != 16 or 0 not in unique_cities or len(tour) != 16 + 1:
        return False, "Tour must include exactly 16 unique cities including city 0"

    # No need to explicitly check requirement 3, it's an optimization goal, not a boolean condition
    return True, "Tour meets all conditions"

def given_solution_validity():
    # Define city coordinates
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # Solution provided
    proposed_tour = [0, 0, 0, 0, 0, 0, 0, 13, 11, 5, 16, 7, 12, 6, 3, 15, 10, 9, 8, 17, 14, 1, 0]
    proposed_cost = 413.2067097300336

    # Validate the tour
    is_valid, message = check_tour_validity(proposed_tour, cities)
    if not is_valid:
        return "FAIL: " + message
    
    # Calculate the actual travel cost from the proposed tour
    actual_cost = 0
    for i in range(len(proposed_tour) - 1):
        actual_cost += calculate_distance(cities[proposed_tour[i]], cities[proposed_tour[i + 1]])
    
    # Check if the calculated cost matches the proposed one
    if not math.isclose(actual_cost, proposed_cost, abs_tol=1e-5):
        return f"FAIL: Calculated cost {actual_cost} does not match proposed cost {proposed_cost}"

    return "CORRECT"

# Run the test
print(given_solution_validity())