import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_tour():
    # City coordinates
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    # City groups
    groups = [
        [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
    ]
    
    # Proposed solution
    tour = [0, 4, 7, 12, 15, 3, 18, 0]
    recorded_cost = 227.40

    # Check if tour starts and ends at the depot
    assert tour[0] == 0 and tour[-1] == 0, "Tour does not start and end at the depot."

    # Check if one city from each group is visited
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # Exclude the depot
        for i, group in enumerate(groups):
            if city in group:
                assert not visited_groups[i], "More than one city from a group is visited."
                visited_groups[i] = True
                break
    assert all(visited_groups), "Not all groups are visited."

    # Check Euclidean distance calculation
    calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    assert abs(calculated_cost - recorded_cost) < 0.1, f"Recorded cost does not match calculated cost. Expected ~{calculated_cost}."

    print("CORRECT")

try:
    test_tour()
except AssertionError as e:
    print("FAIL:", e)