import math

# City coordinates
cities = [
    (14, 77),  # City 0: Depot
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# Provided solution
solution_tour = [0, 6, 2, 13, 8, 9, 14, 0]
provided_cost = 130.67

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Check requirements
def test_solution(tour, cost):
    # [Requirement 1] and [Requirement 4] Check on tour
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    # [Requirement 2]
    if len(set(tour)) != 7:
        return "FAIL"
    # Calculate the total cost from tour
    calc_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    # [Requirement 5] Check the total cost closely matches the provided cost (allowing minor float discrepancies)
    if not math.isclose(calc_cost, cost, rel_tol=1e-2):
        return "FAIL"
    # If all checks pass
    return "CORRECT"

# Running the unit test
test_result = test_solution(solution_tour, provided_cost)
print(test_result)