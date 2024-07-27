import math

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Input coordinates for the cities
coordinates = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Given tour and its claimed total travel cost
tour = [0, 8, 10, 11, 0]
claimed_cost = 110.00961484483386

def verify_tsp_solution(tour, claimed_cost, coordinates):
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 4 cities are visited, including the depot
    if len(tour) != 5:  # Including the return to the start
        return "FAIL"
    
    # Calculate the actual total travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    # Check if the calculated cost matches the claimed cost (allowing a small floating point error margin)
    if not math.isclose(actual_cost, claimed_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the test
test_result = verify_tsp_solution(tour, claimed_cost, coordinates)
print(test_result)