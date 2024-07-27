import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, cost, positions):
    # Verify start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify all cities (1 to 9) are visited exactly once
    visited_cities = sorted(tour[1:-1])  # Ignore the depot city at start and end
    if visited_cities != list(range(1, 10)):
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(positions[tour[i]], positions[tour[i + 1]])
    
    # Compare the provided cost with the calculated cost
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Positions of the cities
positions = [
    (53, 68),  # City 0 (Depot)
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Output from the MILP solution
tour = [0, 6, 1, 7, 9, 2, 5, 3, 8, 4, 0]
total_travel_cost = 278.9348447394249

# Execute verification
verification_result = verify_solution(tour, total_travel_show all_cost, positions)
print(verification_result)