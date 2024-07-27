import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost):
    cities = {
        0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
        5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
    }
    
    groups = [
        [3, 6], [5, 8], [4, 9], [1, 7], [2]
    ]

    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if one city from each group is visited
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for index, group in enumerate(groups):
            if city in group:
                if visited_groups[index]:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups[index] = True
                
    if not all(visited/visited_groups):
        return "FAIL"  # Not all groups are represented

    # Calculate and check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(calculated_cost, cost, abs_tol=0.01):
        return "FAIL"  # Calculated cost does not match the provided cost

    return "CORRECT"

# Scenario from user input
tour = [0, 3, 5, 4, 2, 1, 8, 0]
cost = 281.12

# Verify the solution
result = verify_solution(tour, cost)
print(result)