import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_tour(tour, coordinates):
    # Check if the tour starts and ends at the depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    visited = set(tour)
    if len(visited) != len(coordinates) or any(i not in visited for i in range(len(coordinates))):
        return "FAIL"
    
    # Calculate the travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        actual_cost += calculate_distance(*coordinates[city1], *coordinates[city2])
    
    provided_cost = 290.8376577906224
    
    # Compare calculated cost with provided cost (allowing some margin for floating point precision issues)
    if not math.isclose(actual_cost, provided_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of the cities where index corresponds to city number
coordinates = [
    (53, 68), (75, 11), (91, 95), (22, 80), (18, 63),
    (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)
]

# Provided tour and cost
tour = [0, 5, 3, 8, 4, 6, 1, 7, 9, 2, 0]

# Validation of the provided solution
result = check_tour(tour, coordinates)
print(result)