import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def test_solution():
    # City coordinates
    cities = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
        4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
        8: (61, 90), 9: (42, 49)
    }
    
    # Solution provided
    tour = [0, 9, 3, 8, 4, 2, 1, 6, 7, 5, 0]
    total_travel_cost = 283.76
    max_consecutive_distance = 50.54

    # Verify the tour starts and ends at depot, visits each city once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot city 0."
    if sorted(tour) != sorted(list(set(tour))):
        return "FAIL: Tour does not visit each city exactly once."

    # Calculate actual total travel cost and max consecutive distance
    calculated_cost = 0
    calculated_max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += dist
        if dist > calculated_max_dist:
            calculated_max_dist = dist

    # Check if calculated and reported costs are same
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=0.01):
        return "FAIL: Total travel cost is incorrect."
    if not math.isclose(calculated_max_dist, max_consecutive_distance, abs_tol=0.01):
        return "FAIL: Maximum distance between consecutive cities is incorrect."

    # If all checks pass
    return "CORRECT"

# Run the test function
result = test_solution()
print(result)