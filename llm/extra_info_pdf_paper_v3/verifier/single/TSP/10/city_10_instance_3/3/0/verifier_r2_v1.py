import math

def euclidean_distance(p1, p2):
    # Calculate and return the Euclidean distance between two points
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tsp_solution(cities, tour, reported_cost):
    # Check if the tour is a permutation of all cities and returns to the start
    if sorted(tour[:-1]) != sorted(range(len(cities))) or tour[0] != tour[-1]:
        return "FAIL"
    
    # Calculate the total travel cost based on Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check if the reported total travel cost is close to the calculated cost
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Define coordinates for each city, including the depot
cities = [
    (84, 67),  # Depot: City 0
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

# Tour provided in the problem statement
tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
reported_cost = 315.5597914831042

# Calling the verification function and printing the result
result = verify_tsp_solution(cities, tour, reported_cost)
print(result)