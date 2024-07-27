import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, total_cost):
    # City coordinates
    city_coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # City groups
    city_groups = [
        [5, 6, 16], [8, 18, 19], [11, 12, 13], 
        [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
    ]
    
    # Requirement 1: Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: One city per group
    visited = set(tour[1:-1])
    for group in city_groups:
        if sum(1 for city in group if city in visited) != 1:
            return "FAIL"
        
    # Requirement 3: Calculate travel cost and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(total_cost, calculated_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and total cost
tour = [0, 8, 17, 13, 9, 6, 4, 15, 0]
total_cost = 208.32

# Verify the solution correctness
result = verify_tour(tour, total_cost)
print(result)  # Should print "CORRECT" if everything is ok, otherwise "FAIL"