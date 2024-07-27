import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def test_solution():
    # Environment setup
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57), 
        6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
        12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # Given solution
    tour = [0, 9, 3, 7, 1, 6, 0]
    reported_cost = 118.9
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 6 cities are visited
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Calculate total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Check if the calculated cost matches the reported cost
    # Using a tolerance due to potential floating point arithmetic issues
    if not math.isclose(total_cost, reported_cost, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"

# Run the test function
print(test_solution())