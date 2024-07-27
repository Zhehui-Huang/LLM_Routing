import math

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Defined solution
robot_tours = [
    [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21],
    [1, 2, 5, 7, 9, 10, 8, 6, 3, 4, 11, 13, 16, 14, 0, 12, 15, 18, 20, 17, 21, 19],
    [2, 1, 6, 8, 10, 9, 7, 5, 12, 0, 14, 16, 17, 20, 18, 15, 13, 11, 4, 3, 19, 21],
    [3, 4, 6, 8, 10, 9, 7, 5, 2, 1, 11, 13, 16, 14, 0, 12, 15, 18, 20, 17, 21, 19]
]
reported_costs = [278.55, 240.63, 332.44, 260.94]
total_cost_claimed = 1112.56

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Validate each tour
all_cities_visited = set()
total_calculated_cost = 0
valid_tours = True

try:
    for tour, claimed_cost in zip(robot_tours, reported_costs):
        tour_cost = sum(calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
        total_calculated_cost += tour_cost
        all_cities_visited.update(tour)
        if not math.isclose(tour_cost, claimed_cost, abs_tol=0.1):
            print(f"Tour cost mismatch: Calculated {tour_cost}, Reported {claimed_cost}")
            valid_tours = False
            break

    if valid_tours and len(all_cities_visited) == 22 and all_cities_visited == set(range(22)):
        if math.isclose(total_calculated_cost, total_cost_claimed, abs_tol=0.1):
            print("CORRECT")
        else:
            print(f"FAIL: Total cost mismatch: Calculated {total_calculated_cost}, Claimed {total_cost_claimed}")
    else:
        print("FAIL: Some cities are either not visited or visited more than once.")
except Exception as e:
    print(f"FAIL: An error occurred during validation: {e}")