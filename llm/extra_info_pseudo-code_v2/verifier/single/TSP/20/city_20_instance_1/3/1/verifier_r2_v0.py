import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Provided coordinates
coordinates = [
    (14, 77),  # City 0: Depot
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# Provided Tour
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]

# Tour travel cost stated
stated_total_cost = 477.0516251264448

def verify_tour_requirements(tour, coordinates, stated_cost):
    # Requirement 1: Tour starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once (except depot)
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    
    # Requirement 3: Travel cost calculation
    computed_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    
    # Check computed cost against the given stated cost with a tolerance level
    if not math.isclose(computed_cost, stated_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Print result of verification
print(verify_tour_requirements(tour, coordinates, stated_total_cost))