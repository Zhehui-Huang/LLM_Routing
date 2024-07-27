import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour():
    # City coordinates where the first index is city index (0-indexed)
    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }

    # Provided tour and declared total travel cost
    tour = [0, 11, 1, 8, 14, 5, 3, 4, 10, 9, 7, 13, 12, 6, 2, 0]
    claimed_total_cost = 340.4418416526355

    # Verify the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Ensure all cities are visited exactly once, excluding the start/end city
    visits = {}
    for city in tour:
        if city in visits:
            visits[city] += 1
        else:
            visits[city] = 1
            
    if visits[0] != 2 or any(visits[city] != 1 for city in range(1, 15)):
        return "FAIL"

    # Calculate the total travel distance of the provided tour
    total_distance = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        total_distance += calculate_euclidean_distance(*cities[city_a], *cities[city_b])

    # Compare the calculated total cost to the claimed one.
    if not math.isclose(total_distance, claimed_total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Execute the verification function
result = verify_tour()
print(result)