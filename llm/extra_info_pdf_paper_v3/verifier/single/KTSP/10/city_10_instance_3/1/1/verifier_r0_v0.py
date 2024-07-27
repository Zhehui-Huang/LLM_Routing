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

    # Ensure the tour starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Ensure exactly 7 unique cities are visited, including the depot
    if len(set(tourney)) != 7:
        return "FAIL"

    # Calculate the actual travel cost from the tour and compare with given total_travel_cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += distance(cities[tour[i]], cities[tour[i + 1]])
    
    if actual_cost != total_travel_cost:
        return "FAIL"

    return "CORRECT"

# Example test case
tour_solution = []  # Provided solution
total_travel_cost_solution = float('inf')  # Provided cost

# Verify the solution
print(verify_tour(tour_solution, total_travel_cost_solution))