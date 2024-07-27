import math

# Data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

tours = [
    [0, 0], [1, 10, 1], [2, 13, 2], [3, 8, 12, 3],
    [4, 11, 15, 4], [5, 14, 5], [6, 6], [7, 9, 7]
]

solution_costs = [0.0, 14.142135623730951, 18.110770276274835, 33.94039963350503,
                  26.480522629341756, 16.97056274847714, 0.0, 20.09975124224178]

# Verify tours
def verify_tours():
    all_visited = [False] * len(coordinates)
    for tour in tours:
        if tour[0] != tour[-1] or tour.count(tour[0]) != 2:
            return False
        for city in tour[1:-1]:
            if all_visited[city]:
                return False
            all_visited[city] = True
    return all(all_visited)

# Calculate and verify costs
def calculate_and_verify_costs():
    total_calculated_cost = 0
    for tour, given_cost in zip(tours, solution_costs):
        tour_cost = 0
        for i in range(len(tour) - 1):
            x1, y1 = coordinates[tour[i]]
            x2, y2 = coordinates[tour[i+1]]
            tour_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if not math.isclose(tour_cost, given_cost, rel_tol=1e-9):
            return False
        total_calculated_cost += tour_cost
    overall_cost = sum(solution_costs)
    if not math.isclose(total_calculated_cost, overall_cost, rel_tol=1e-9):
        return False
    return True

# Run tests
if verify_tours() and calculate_and_verify_costs():
    print("CORRECT")
else:
    print("FAIL")