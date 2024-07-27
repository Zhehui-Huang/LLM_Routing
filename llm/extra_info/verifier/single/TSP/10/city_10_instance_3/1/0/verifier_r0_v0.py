import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, proposed_cost, coordinates):
    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify all cities except depot are visited exactly once
    visited_cities = tour[1:-1]
    if sorted(visited_cities) != list(range(1, 10)):
        return "FAIL"
    
    # Calculate and verify the total cost of the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    if not math.isclose(total_cost, proposed_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and total travel cost
tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
proposed_cost = 315.56

# Coordinates of cities
coordinates = [
    (84, 67),  # City 0 (depot)
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

# Validate the solution
result = verify_tour(tour, proposed_cost, coordinates)
print(result)