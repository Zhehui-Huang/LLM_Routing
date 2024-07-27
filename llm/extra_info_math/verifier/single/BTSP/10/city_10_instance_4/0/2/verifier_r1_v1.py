import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(coordinates, tour, total_cost, max_dist):
    # [Requirement 1] Check if number of cities including the depot is 10
    if len(coordinates) != 10:
        return "FAIL"

    # [Requirement 2] Check if the tour starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 3] Check if each city (except depot) is visited exactly once
    visited = set(tour[1:-1])  # exclude starting and ending depot
    if len(visited) != len(coordinates) - 1 or any(city not in visited for city in range(1, 10)):
        return "FAIL"

    # Calculate the total travel cost from the tour
    calculated_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
    
    # [Requirement 5] Check the total_cost matches the Euclidean distance total for the provided tour
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-6):
        return "FAIL"

    # [Requirement 6] Check the maximum distance between any two consecutive cities
    calculated_max_dist = max(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
    if not math.isclose(calculated_max_dist, max_dist, rel_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Define coordinates of each city including the depot
coordinates = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Details from the solver output
tour = [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0]
total_travel_cost = 143.17821063276352
max_distance = 14.317821063276353

# Verify the solution
result = verify_solution(coordinates, tour, total_travel_cost, max_distance)
print(result)