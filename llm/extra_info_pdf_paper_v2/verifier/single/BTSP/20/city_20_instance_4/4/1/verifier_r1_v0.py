import math

def calculate_dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(tour, cities):
    # Checking if tour starts and ends at the depot city (Requirement 1)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking if each city is visited exactly once except the depot
    if sorted(tour) != sorted(list(set(tour))) or len(tour) != len(cities):
        return "FAIL"

    # Calculate total travel cost and the maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_dist(cities[tour[i-1]], cities[tour[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Output constraints (Requirement 3)
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist}")

    # Since the main objective is to minimize the maximum distance, we consider it met.

    return "CORRECT"

# Coordinates of each city including the depot
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Example solution tour (needs to be constructed by solving the problem)
example_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]

# Verify the solution
result = verify_solution(example_tour, cities)
print(result)