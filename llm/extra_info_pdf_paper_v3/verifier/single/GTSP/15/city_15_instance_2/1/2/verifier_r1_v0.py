import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def is_tour_correct(tour, cost):
    cities = {0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
              5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
              10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)}

    groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]

    # Check that the robot starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Check that the robot visits exactly one city from each group
    visited_groups = [0 for _ in groups]
    for city in tour[1:-1]:  # Ignore the depot city at start and end
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1

    if any(count != 1 for count in visited_groups):
        return False

    # Calculate the travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check the total travel cost (rounding to handle floating point arithmetic)
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return False

    # If all checks pass
    return True

# Test data from the task
tour = [0, 12, 10, 4, 3, 2, 0]
cost = 138.15

# Check if the provided solution is correct
if is_tour_correct(tour, cost):
    print("CORRECT")
else:
    print("FAIL")