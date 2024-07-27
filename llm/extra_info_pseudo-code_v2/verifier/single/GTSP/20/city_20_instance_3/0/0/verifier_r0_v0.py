import math

# City coordinates
city_coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Groups
city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Provided solution
solution_tour = [0, 0, 6, 2, 8, 4, 1, 0]
provided_cost = 242.50

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour, expected_cost):
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Check if exactly one city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city in tour:
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups[i] += 1
                if visited_groups[i] > 1:
                    return False
    if any(v != 1 for v in visited_groups if city_groups.index(group) != 0):
        return False

    # Calculate the cost of the provided tour
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_euclidean_distance(tour[i], tour[i + 1])

    # Check if calculated cost is close to the provided expected cost (due to float precision issues)
    if not math.isclose(actual_cost, expected_cost, rel_tol=1e-5):
        return False

    return True

# Run the validation
if validate_tour(solution_tour, provided_cost):
    print("CORRECT")
else:
    print("FAIL")