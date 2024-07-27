import pytest
import math

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Mapping city coordinates (for the test environment based on example)
coordinates = [
    (30, 56), # City 0: Depot
    (53, 42), # City 1
    (1, 95),  # City 2
    (25, 61), # City 3
    (69, 57), # City 4
    (6, 58),  # City 5
    (12, 84), # City 6
    (72, 77), # City 7
    (98, 95), # City 8
    (11, 0),  # City 9
    (61, 25), # City 10
    (52, 0),  # City 11
    (60, 95), # City 12
    (10, 94), # City 13
    (96, 73), # City 14
    (14, 47), # City 15
    (18, 16), # City 16
    (4, 43),  # City 17
    (53, 76), # City 18
    (19, 72)  # City 19
]

# City groups
city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Placeholder for the provided solution's tour and its cost calculation function
# Replace `solution_tour` with the actual tour from the solution
solution_tour = [0, 4, 6, 9, 2, 1, 8, 0]
solution_cost = sum(euclidean_distance(coordinates[solution_tour[i]], coordinates[solution_tour[i + 1]]) for i in range(len(solution_tour) - 1))

def test_solution():
    # Test 1: Start and end at the depot city 0
    assert solution_tour[0] == 0 and solution_tour[-1] == 0, "Tour must start and end at the depot city 0."
    
    # Test 2: Visit exactly one city from each of the 6 city groups
    visited_groups = [0] * len(city_groups)
    for city in solution_tour[1:-1]:
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups[i] += 1
    assert all(count == 1 for count in visited_groups), "One city from each city group must be visited exactly once."

    # Test 3: Ensure the tour uses Euclidean distance
    computed_cost = sum(euclidean_distance(coordinates[solution_tour[i]], coordinates[solution_tour[i + 1]]) for i in range(len(solution_tour) - 1))
    assert solution_cost == computed_cost, "The travel cost must be correctly computed using the Euclidean distance."

    return "CORRECT"

# Run the test
test_result = test_solution()
print(test_result)