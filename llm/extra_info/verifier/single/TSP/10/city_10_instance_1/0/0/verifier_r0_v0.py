import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def test_tsp_solution():
    cities = [
        (53, 68),  # Depot city 0
        (75, 11),  # City 1
        (91, 95),  # City 2
        (22, 80),  # City 3
        (18, 63),  # City 4
        (54, 91),  # City 5
        (70, 14),  # City 6
        (97, 44),  # City 7
        (17, 69),  # City 8
        (95, 89)   # City 9
    ]

    tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
    claimed_total_distance = 278.9348447394249

    # Checking if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking if the tour visits all cities exactly once, except the depot which should be visited twice (start, end)
    if sorted(tour[1:-1]) != sorted(range(1, 10)):
        return "FAIL"

    # Compute the total distance of the tour
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean(distance(cities[tour[i]], cities[tour[i + 1]]))

    # Check if the computed distance matches the claimed total distance
    if not math.isclose(total_distance, claimed_total_distance, rel_tol=1e-5):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Run test
print(test_tsp_solution())