import math

# Define the Euclidean distance calculator
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Coordinates of each city (depot city included at index 0)
city_coordinates = [
    (9, 93),   # City 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Suggested tour and its claimed cost
suggested_tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
claimed_cost = 373.97

def verify_tour(tour, claimed_cost):
    # Requirement 1: Start and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit all cities exactly once (ignoring first and last as they are depot)
    if set(tour[1:-1]) != set(range(1, 15)):
        return "FAIL"

    # Calculate the tour's actual travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Compare the calculated to the claimed costs, allowing small precision errors
    if not math.isclose(actual_cost, claimed_cost, rel_tol=1e-5):
        return "FAIL"

    # If all verifications pass
    return "CORRECT"

# Run the test
result = verify_tour(suggested_tour, claimed_cost)
print(result)  # Output should be "CORRECT" or "FAIL" based on the verification