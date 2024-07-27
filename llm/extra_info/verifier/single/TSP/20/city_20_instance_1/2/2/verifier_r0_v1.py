import math

def calculate_total_distance(tour, positions):
    def euclidean_distance(city1, city2):
        return math.sqrt((positions[city1][0] - positions[city2][0])**2 + (positions[city1][1] - positions[city2][1])**2)

    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    return total_distance

def test_tour(tour, total_distance_claimed):
    positions = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
        (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
        (78, 76), (68, 45), (50, 28), (69, 9)
    ]
    
    # Requirement 1
    assert tour[0] == 0 and tour[-1] == 0, "Tour does not start/end at depot city."
    
    # Requirement 2
    visited = sorted(tour[1:-1])
    expected = list(range(1, 20))
    assert visited == expected, "Each city must be visited once excluding the depot."
    
    # Requirement 3
    actual_total_distance = calculate_total_distance(tour, positions)
    assert math.isclose(actual_total_user, total_distance_claimed, rel_tol=1e-9), "Total travel cost does not match."
    
    print("Tests passed!")

# Input data from the solution
my_tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
my_total_cost = 477.0516251264448

# Execute the tests
try:
    test_tour(my_tour, my_total_cost)
    print("CORRECT")
except AssertionError as e:
    print("FAIL:", str(e))