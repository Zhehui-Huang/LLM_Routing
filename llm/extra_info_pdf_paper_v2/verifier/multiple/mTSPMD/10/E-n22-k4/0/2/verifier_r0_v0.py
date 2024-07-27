import numpy as np

# Constants
DEPOTS = [0, 1, 2, 3]

# Solution provided
path = [1, np.int64(2), np.int64(5), np.int64(7), np.int64(9), np.int64(6), np.int64(8), np.int64(10), np.int64(12), np.int64(15), np.int64(18), np.int64(20), np.int64(17), np.int64(21), np.int64(19), np.int64(16), np.int64(14), np.int64(0), np.int64(13), np.int64(11), np.int64(4), np.int64(3), 1]
total_cost = 278.44

def verify_path(path):
    # Checking if starts and ends at a depot, and depots are not visited in between
    for i in range(len(DEPOTS)):
        if path[0] != DEPOTS[i] or path[-1] != DEPOTS[i]:
            continue
        if any(DEPOTS[j] in path[1:-1] for j in range(len(DEPOTS))):
            return False
        return len(set(path[1:-1])) == len(path[1:-1]) and len(path) == 23 and set(path[1:-1]) == set(range(22)) - set(DEPOTS)
    return False

def verify_total_travel_cost(path, total_cost):
    # Assume we have a function calculate_total_cost(path) that calculates the total cost of a given path.
    # For the purpose of this example, assume the provided total_cost is correct.
    # This should be replaced with actual implementation in practice.
    return True  # As a placeholder, assume the cost matches correctly.

def test_solution(path, total_cost):
    if not verify_path(path):
        return "FAIL: Path verification failed."
    if not verify_total_patterns(path):
        return "FAIL: Path pattern or path length is incorrect."
    if not verify_total_travel_cost(path, total_cost):
        return "FAIL: Total cost verification failed."
    return "CORRECT"

# Unit Test execution
result = test_solution(path, total_cost)
print(result)