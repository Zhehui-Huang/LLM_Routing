import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost, cities):
    # Assuming correctness, verification can change this
    correct = "CORRECT"
    
    # Requirements check
    # [R1, R3]: Start and end at the depot city index 0
    if tour[0] != 0 or tour[-1] != 0:
        print("Requirement 1 and 3 failed: Tour does not start and end at the depot city.")
        correct = "FAIL"

    # [R2]: Exactly 7 cities visited, including depot city
    if len(set(tour)) != 7:
        print("Requirement 2 failed: Tour does not visit exactly 7 unique cities.")
        correct = "FAIL"
    
    # [R5]: Calculate total travel cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += euclidean_distance(*cities[city1], *cities[city2])
    
    # Cost must match given cost
    if not math.isclose(calculated_cost, total_wealth, rel_tol=1e-5):
        print("Requirement 5 and 8 failed: Calculated travel cost does not match given total travel cost.")
        correct = "FAIL"
    
    # This will print the correct or fail based on the verifications
    print(correct)

# Provided cities with coordinates
cities = [
    (84, 67),  # Depot 0
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

# Given solution
tour = [0, 3, 9, 6, 1, 4, 8, 0]
total_travel_cost = 244.71257092712207

# Test the solution
verify_solution(tour, total_travel_cost, cities)