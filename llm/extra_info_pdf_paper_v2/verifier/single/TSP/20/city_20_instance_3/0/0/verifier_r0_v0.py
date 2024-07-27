import math

# Provided tour and total cost
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
provided_total_cost = 458.37

# City positions
positions = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_tour(tour, positions, provided_total_cost):
    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2 & 4
    if sorted(tour[1:-1]) != list(range(1, len(positions))):
        return "FAIL"
    
    # Requirement 3
    if tour[-1] != 0:
        return "FAIL"
    
    # Requirement 5 & 6
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(positions[tour[i]], positions[tour[i+1]])
    
    # Comparing provided and calculated cost by rounding to 2 decimals
    if not math.isclose(provided_total_cost, round(calculated_one_cost, 2), rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Running the test
result = test_tour(tour, positions, provided_total_cost)
print(result)