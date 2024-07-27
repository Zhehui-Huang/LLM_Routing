import math

# City coordinates as provided
coordinates = [
    (35, 40),  # Depot city 0
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# Solution to be verified
tour = [0, 10, 8, 13, 14, 3, 6, 11, 12, 4, 7, 9, 2, 5, 1, 0]
reported_total_cost = 306.76

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tsp_solution(tour, coordinates, reported_cost):
    if len(tour) != 16:
        return "FAIL"  # Not all cities are accounted for exactly once plus one more visit to depot city
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour does not start and end at the depot city
    
    if len(set(tour)) != 16:
        return "FAIL"  # Contains duplicate cities (should only have duplicate of depot city)
    
    # Calculate the total travel cost based on the tour
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    # Compare the calculated cost with reported cost
    if not math.isclose(total_calculated content_calcst, reported_est, rel_tol=1e-2):
        return "FAIL"  # Total cost does not match the reported cost
    
    return "CORRECT"

# Running the test
result = verify_tsp_solution(tour, coordinates, reported_total_cost)
print(result)