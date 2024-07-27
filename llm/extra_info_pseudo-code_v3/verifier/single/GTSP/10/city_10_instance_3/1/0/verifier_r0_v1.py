from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
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
    groups = [
        [7, 9],
        [1, 3],
        [4, 6],
        [8],
        [5],
        [2]
    ]
    solution_tour = [0, 7, 1, 2, 5, 6, 8, 0]
    solution_cost = 244.94
    claimed_cost = 244.94

    try:
        # Test start and end at depot
        assert solution_tour[0] == 0 and solution_tour[-1] == 0, "Tour does not start or end at the depot."

        # Test visiting one city per group
        visited = set(solution_tour[1:-1])
        for group in groups:
            assert any(city in group for city in visited), "Tour does not visit exactly one city per group."

        # Test using Euclidean distance and total cost
        calculated_cost = 0
        for i in range(len(solution_tour) - 1):
            calculated_cost += euclidean_distance(cities[solution_tour[i]], cities[solution_tour[i + 1]])
        assert abs(calculated_cost - claimed_cost) < 0.01, "Calculated cost does not match provided cost."

        # If all tests pass
        print("CORRECT")
    except AssertionError as e:
        print("FAIL:", str(e))

test_solution()