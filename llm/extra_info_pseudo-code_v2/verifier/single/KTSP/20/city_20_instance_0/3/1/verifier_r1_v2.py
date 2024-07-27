import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def verify_solution(tour, total_travel_cost):
    coordinates = [
        (8, 11),   (40, 6),  (95, 33), (80, 60),
        (25, 18),  (67, 23), (97, 32), (25, 71),
        (61, 16),  (27, 91), (91, 46), (40, 87),
        (20, 97),  (61, 25), (5, 59),  (62, 88),
        (13, 43),  (61, 28), (60, 63), (93, 15)
    ]

    # Verify tour starts and ends at the depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL - Tour does not start and end at depot."

    # Verify exactly 4 cities are visited including the depot
    if len(tour) != 5:
        return "FAIL - Tour does not include exactly 4 cities including the depot."

    # Verify the total travel cost
    calculated_cost = calculate_total_travel_cost(tour, coordinates)
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return f"FAIL - Incorrect total travel cost: expected {total_travel_cost}, got {calculated_cost}"

    return "CORRECT - All requirements met."

# Example inputs
tour_example = [0, 1, 8, 4, 0]
total_travel_cost_example = 110.08796524611944

# Call the verification function
result = verify_solution(tour_example, total_travel_cost_example)
print(result)