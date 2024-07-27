import math

def calculate_distance(city_a, city_b):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = city_a
    x2, y2 = city_b
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(tour, cities):
    """Validate the robot tour based on the requirements."""
    # Requirement 1: Starting and ending at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start and end at the depot city"

    # Requirement 2: All cities are visited exactly once, except depot which is visited twice (start and end)
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL", "Tour does not visit all cities exactly once"
    
    # Calculate total travel cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Requirement 5: Include total travel cost in the output
    expected_total_cost = 458.36719998557066
    if not math.isclose(total_cost, expected_total_cost, abs_tol=0.001):
        return "FAIL", f"Incorrect total travel cost: {total_cost} (expected around {expected_total_cost})"

    # Requirement 6: Include maximum distance between any two consecutive cities in the tour
    expected_max_distance = 68.15423684555495
    if not math.isclose(max_distance, expected_max_distance, abs_tol=0.001):
        return "FAIL", f"Incorrect maximum distance between cities: {max_distance} (expected around {expected_max_b}instance)"

    return "CORRECT", None  # Pass all checks

# Define the city coordinates as per the environment information   
cities = [
    (30, 56),  # Depot city 0
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
    (19, 72)   # City 19
]

# Solution provided
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]

# Validate the provided tour
result, message = validate_tour(tour, cities)
if result == "CORRECT":
    print("CORRECT")
else:
    print("FAIL")
    print(message)