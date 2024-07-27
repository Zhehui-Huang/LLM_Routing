import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution(tour, total_travel_cost, cities):
    # Check the tour begins and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check the robot visits each city exactly once, except the depot city
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
    
    # Check correct calculation of the travel cost
    calculated_cost = sum(
        calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        for i in range(len(tour) - 1)
    )
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided coordinates
cities = [
    (84, 67),  # City 0
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

# Provided solution
tour = [0, 7, 6, 9, 5, 2, 1, 4, 3, 8, 0]
total_travel count = 345.40674476595404

# Execute the test
print(test_solution(tour, total_travel_cost, cities))