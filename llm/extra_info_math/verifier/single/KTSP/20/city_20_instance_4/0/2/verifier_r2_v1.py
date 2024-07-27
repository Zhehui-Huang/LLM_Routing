import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, reported_cost):
    coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]

    # Check Requirement 1: Starts and ends at depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL: Tour does not start and end at depot city 0."
    
    # Check Requirement 2: Visits exactly 16 cities, including the depot
    if len(tour) != 17 or len(set(tour)) != 17:
        return "FAIL: Tour does not visit exactly 16 cities including the depot."

    # Calculate the travel cost
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    # Check Requirement 4: Correct calculation of distances
    if not math.isclose(cost, reported_cost, abs_tol=1e-2):
        return f"FAIL: Reported travel cost is incorrect. Calculated: {cost}, Reported: {reported_cost}"

    return "CORRECT"

# Provided tour and cost
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 0]
reported_cost = 285.96

# Check solution
result = verify_solution(tour, reported_cost)
print(result)