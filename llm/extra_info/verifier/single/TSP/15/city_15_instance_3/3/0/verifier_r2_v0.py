import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Define cities based on the given data
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def test_route():
    proposed_tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
    proposed_distance = 373.61

    # Check if the tour starts and ends at the depot city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once
    unique_cities = set(proposed_tour[1:-1])
    if len(unique_cities) != 14 or sorted(unique_cities) != list(range(1, 15)):
        return "FAIL"

    # Calculate total travel cost and compare with proposed_distance
    total_distance = 0
    for i in range(len(proposed_tour) - 1):
        total_distance += euclidean_distance(cities[proposed_tour[i]], cities[proposed_tour[i+1]])
    if abs(total_distance - proposed_distance) > 0.01:  # Allowing a small margin due to rounding issues
        return "FAIL"

    return "CORRECT"

# Run the test
print(test_route())