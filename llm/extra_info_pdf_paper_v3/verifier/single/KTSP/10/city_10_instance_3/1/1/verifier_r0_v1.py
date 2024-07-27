def distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    from math import sqrt
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, total_travel_cost):
    # List of city coordinates; index correlates with city number.
    cities = [
        (84, 67),  # City 0: Depot
        (74, 40),  # City 1
        (71, 13),  # City 2
        (74, 82),  # City 3
        (97, 28),  # City 4
        (0, 31),   # City 5
        (8, 62),   # City 6
        (74, 56),  # City 7
        (85, 71),  # City 8
        (6, 76)    # City 9
    ]

    # Check for an empty tour or insufficient tour length
    if not tour or len(tour) < 2:
        return "FAIL"

    # Ensure the tour starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Ensure exactly 7 unique cities are visited, including the depot.
    # 'set' is used to ignore duplicates.
    if len(set(tour)) != 7 or len(tour) < 8:  # including depot twice, start and end.
        return "FAIL"

    # Calculate the actual travel cost from the tour and compare with given total_travel_cost
    actual_cost = 0
    try:
        for i in range(len(tour) - 1):
            actual_cost += distance(cities[tour[i]], cities[tour[i + 1]])
    except IndexError:
        # This handles the case if an invalid city index is in the tour list
        return "FAIL"
    
    # Validate calculated distance matches the provided total travel cost,
    # allow some tolerance for floating-point arithmetic.
    if not abs(actual_cost - total_travel_cost) < 1e-5:
        return "FAIL"

    return "CORRECT"

# Example test case
tour_solution = []  # Provided solution
total_travel_cost_solution = float('inf')  # Provided cost

# Verify the solution
print(verify_tour(tour_solution, total_travel_cost_solution))