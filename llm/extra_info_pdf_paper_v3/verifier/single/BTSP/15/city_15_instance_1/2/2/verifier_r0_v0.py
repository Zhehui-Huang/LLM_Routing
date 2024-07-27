import math

# Given cities coordinates
cities_coordinates = [
    (29, 51),  # City 0 (depot)
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once plus the return to the depot
    if sorted(tour) != sorted([0] + list(range(1, len(cities_coordinates)))):
        return "FAIL"

    # Check if the Euclidean distances match the problem constraints
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        from_city = tour[i]
        to_city = tour[i + 1]
        distance = calculate_distance(cities_coordinates[from_city], cities_coordinates[to_city])
        total_distance += distance
        max_distance = max(max_distance, distance)
    
    # Round values because the provided values (442.57, 85.21) are likely rounded
    if round(total_distance, 2) != 442.57 or round(max_distance, 2) != 85.21:
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Provided solution tour
solution_tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
# Verify the solution
result = verify_tour(solution_tour)
print(result)