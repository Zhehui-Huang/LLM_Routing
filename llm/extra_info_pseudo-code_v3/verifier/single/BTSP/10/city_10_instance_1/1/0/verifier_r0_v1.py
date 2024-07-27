import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, reported_total_cost, reported_max_distance):
    coordinates = [
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

    # Check if starting and ending at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check all cities are visited exactly once
    if sorted(tour[:-1]) != list(range(len(coordinates))):
        return "FAIL"

    # Calculate total cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Verify reported maximum distance and total cost
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-5) or \
       not math.isclose(max_distance, reported_max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 291.41088704894975
maximum_distance = 56.61271941887264

# Call verification function
result = verify_solution(tour, total_travel_cost, maximum_distance)
print(result)