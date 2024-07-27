import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities):
    # Verify the robot visits all cities exactly once and returns to the depot
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"

    # Verify the tour starts and ends at the depot city, which is city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Compute the total euclidean distance
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
    # The reported travel cost
    reported_cost = 269.28

    # Check if the calculated distance matches the reported total travel cost (within a small error margin)
    if not math.isclose(total_distance, reported_cost, rel_tol=1e-3):
        return "FAIL"

    # Implicitly by constructing the tour properly, the binary constraints and subtour elimination are enforced
    return "CORRECT"

# City coordinates as given
cities = [
    (9, 93),   # City 0: Depot
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Tour as reported by the solver (includes an error)
reported_tour = [0, 2, 6, 5, 3, 13, 7, 4, 12, 14, 11, 9, 1, 10, 8]

# Verify the solution
result = verify_solution(reported_tour, cities)
print(result)