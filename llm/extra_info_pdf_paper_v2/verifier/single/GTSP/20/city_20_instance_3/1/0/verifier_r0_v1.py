import math

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Coordinates from the problem description
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# City groups
city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Placeholder for the solution's tour
# Note: Update this list with the correct tour solution obtained.
solution_tour = [0, 4, 6, 9, 2, 1, 8, 0]  # Example tour, replace with actual output

def test_solution():
    # Start and end at the depot
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL: The tour must start and end at the depot city 0."

    # Visit exactly one city from each group
    visited = [0] * len(city_groups)
    for city in solution_tour[1:-1]:
        for index, group in enumerate(city_groups):
            if city in group:
                visited[index] += 1
    if any(v != 1 for v in visited):
        return "FAIL: One city from each city group must be visited exactly once."

    # Check the travel cost computation
    computed_cost = sum(euclidean_distance(coordinates[solution_tour[i]], coordinates[solution_tour[i+1]])
                        for i in range(len(solution_tour) - 1))
    # You would need the solution's stated cost for an exact comparison
    # If `solution_cost` is the specified travel cost:
    # solution_cost = some_computed_value
    # if computed_cost != solution_cost:
    #    return "FAIL: Travel costs must match."

    return "CORRECT"

result = test_solution()
print(result)