import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_tour():
    # The provided solution
    tour = [0, 10, 15, 3, 5, 14, 13, 18, 0]
    claimed_cost = 231.14
    
    # City coordinates
    coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
        (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
        (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # Group definition
    groups = [
        [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
    ]
    
    # Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if only one city from each group is visited
    group_visit_count = [0] * len(groups)
    for city in tour[1:-1]:  # exclude the starting and ending depot city
        for i, group in enumerate(groups):
            if city in group:
                group_visit_count[i] += 1
    
    if any(count != 1 for count in group_visit_count):
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    actual_cost = 0.0
    for i in range(len(tour) - 1):
        actual_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Check if calculated cost matches the claimed cost
    if not math.isclose(actual_cost, claimed_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
print(test_tour())