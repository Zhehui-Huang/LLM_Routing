import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_cost(tour, cost, coordinates):
    """ Verify if the tour and cost satisfy the problem requirements. """
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot."
    
    # Check if all cities are visited exactly once, except the depot
    if sorted(tour) != sorted(list(set(tour))):
        return "FAIL: Each city must be visited exactly once."
    
    # Calculate the total travel cost and compare with provided cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        x1, y1 = coordinates[tour[i-1]]
        x2, y2 = coordinates[tour[i]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return f"FAIL: Calculated cost {calculated_cost} does not match provided cost {cost}."

    return "CORRECT"

# Coordinates of cities including depot
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Provided tour and total travel cost
tour_solution = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 19, 15, 18, 8, 1, 13, 12, 9, 2, 6, 0]
total_travel_cost = 389.99

# Run the verification function
result = verify_tour_and_cost(tour_solution, total_travel_cost, coordinates)
print(result)