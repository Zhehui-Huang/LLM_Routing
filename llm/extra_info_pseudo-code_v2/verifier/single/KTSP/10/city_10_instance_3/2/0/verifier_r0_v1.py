import math

# Provided solution details
tour = [0, 4, 2, 1, 7, 3, 8, 0]
total_cost = 159.97188184793015

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def calculate_euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def verify_tour(tour, total_cost, cities):
    # Verify the tour starts and ends at the depot, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify exactly 7 unique cities are visited (excluding the start/end at depot)
    if len(set(tour) - {0}) != 6:
        return "FAIL"
    
    # Verify the cost is computed correctly
    calculated_cost = 0
    for i in range(len(tour)-1):
        city_a = cities[tour[i]]
        city_b = cities[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(city_a, city_b)
    
    # Check if the provided total cost matches the calculated cost
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
test_result = verify_tour(tour, total_cost, cities)
print(test_result)