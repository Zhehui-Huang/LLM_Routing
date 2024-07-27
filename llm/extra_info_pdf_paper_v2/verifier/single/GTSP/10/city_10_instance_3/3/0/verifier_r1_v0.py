import math

# Define unit tests
def test_robot_tour(tour, total_cost):
    # Provided cities and groups
    cities = {
        0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82),
        4: (97, 28), 5: (0, 31), 6: (8, 62), 7: (74, 56),
        8: (85, 71), 9: (6, 76)
    }
    groups = [
        [7, 9],  # Group 0
        [1, 3],  # Group 1
        [4, 6],  # Group 2
        [8],     # Group 3
        [5],     # Group 4
        [2]      # Group 5
    ]
    
    def euclidean_distance(city1, city2):
        return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    
    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify the tour visits exactly one city from each group
    visited = set(tour[1:-1])  # exclude starting and ending depot city
    for group in groups:
        if not visited.intersection(set(group)):
            return "FAIL"
    
    # Verify the total travel cost is calculated using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Given solution data
given_tour = [0, 7, 1, 4, 8, 5, 2, 0]
given_total_cost = 324.1817486177585

# Run the unit test
output = test_robot_tour(given_tour, given_total_cost)
print(output)