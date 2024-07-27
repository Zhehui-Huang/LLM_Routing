import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tsp_solution(cities, tour, reported_cost):
    # Verify all cities are visited exactly once and return to depot
    if sorted(tour[:-1]) != sorted(range(len(cities))) or tour[0] != tour[-1]:
        return "FAIL"
    
    # Calculate total cost using Euclidean distance
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean distance(cities[tour[i]], cities[tour[i+1]])

    # Check if the calculated cost matches the reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    # Check if the solution is a Hamiltonian circuit (trivially true if the above conditions are met)
    return "CORRECT"

# Cities coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Provided tour and reported cost
tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
reported_cost = 315.5597914831042

# Execute verification
result = verify_tsp_solution(cities, tour, reported_cost)
print(result)