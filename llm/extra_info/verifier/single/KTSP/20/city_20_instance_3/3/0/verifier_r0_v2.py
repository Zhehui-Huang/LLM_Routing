import math

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_total_travel_cost(cities, tour):
    """Calculate the total travel cost for a given tour using the cities' coordinates."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def test_solution():
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
        (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
        (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
        (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    proposed_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 11, 10, 1, 0]
    proposed_cost = 254.73018946347761

    # Requirement 1: Start and end at depot city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Tour must include exactly 13 cities including the depot
    if len(set(proposed_tour)) != 13:
        return "FAIL"

    # Requirement 3: Verify total travel cost
    computed_cost = calculate_total_travel_cost(cities, proposed_tour)
    # Allow a small numerical difference since floating-point arithmetic can introduce tiny variations
    if abs(computed_cost - proposed_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Output the result of the test
print(test_solution())