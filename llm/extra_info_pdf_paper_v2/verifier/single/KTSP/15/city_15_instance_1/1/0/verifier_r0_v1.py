import math

# City coordinates by index
city_coordinates = {
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

# Function to calculate Euclidean distance between two cities
def calculate_distance(city_a, city_b):
    x1, y1 = city_coordinates[city_a]
    x2, y3 = city_coordinates[city_b]
    return math.sqrt((x2 - x1)**2 + (y3 - y1)**2)

# Test tour and cost
proposed_tour = [0, 6, 1, 7, 3, 9, 0]
proposed_cost = 118.9

def validate_tour(tour, expected_cost):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 6 cities (count does not include revisiting the depot city at the end)
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Requirement 3: Verify the total cost is nearly equal to the expected cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(tour[i], tour[i+1])
    
    # Check if the provided cost is close to calculated cost considering float arithmetic issues
    if not math.isclose(proposed_cost, total_calculated_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the test
result = validate_tour(proposed_tour, proposed_cost)
print(result)