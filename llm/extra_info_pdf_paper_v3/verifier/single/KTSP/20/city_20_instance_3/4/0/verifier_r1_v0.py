import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_tour_and_cost(tour, total_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour must start and end at the depot (city 0)"
    if len(tour) != 14:  # 13 cities + returning to the depot
        return "FAIL", f"Tour must include exactly 13 cities and return to depot, found {len(tour)-1} cities"
    if len(set(tour)) < 14 or len(tour) != len(set(tour)):
        return "FAIL", "Tour contains duplicate cities or does not cover all mentioned cities."
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL", f"Calculated total cost {calculated_cost} does not match provided cost {total_cost}"
    return "CORRECT", "All checks passed."

def test_solution():
    # City coordinates as described in the problem (0-indexed positions)
    cities = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
        6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
        12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16),
        17: (4, 43), 18: (53, 76), 19: (19, 72)
    }

    # Given solution
    tour = [0, 1, 19, 15, 17, 3, 6, 13, 2, 18, 12, 7, 16, 0]
    total_cost = 402.34  # Provided total travel cost
    
    # Perform checks
    status, message = check_tour_and_cost(tour, total_cost, cities)
    print(status)  # Output based on the results of the checks
    if status == "FAIL":
        print(message)  # Provide reasoning if failed

test_solution()