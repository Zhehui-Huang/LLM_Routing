import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_cost):
    cities = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
        4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
        8: (61, 90), 9: (42, 49)
    }

    # [Requirement 1] Start at depot city 0
    if tour[0] != 0:
        return "FAIL"

    # [Requirement 2] Visit all cities exactly once, except for the depot, before returning to the depot
    cities_visited = tour[1:-1]  # exclude the initial and final depot visit
    if sorted(cities_visited) != list(range(1, 10)):
        return "FAIL"
    
    # [Requirement 3] After visiting all cities, return to the depot city 0
    if tour[-1] != 0:
        return "FAIL"

    # [Requirement 4] Calculate the total travel cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        city1 = tour[i]
        city2 = tour[i+1]
        calculated_cost += euclidean_distance(*cities[city1], *cities[city2])

    # Check the provided total cost and match with calculated cost
    if not (abs(calculated_cost - total_cost) < 1e-6):  # small tolerance due to floating point arithmetic
        return "FAIL"

    return "CORRECT"

# Example solution provided
tour = [0, 5, 9, 4, 8, 3, 2, 1, 6, 7, 0]
total_cost = 271.4716218753353

# Verify solution
print(verify_solution(tour, total_cost))