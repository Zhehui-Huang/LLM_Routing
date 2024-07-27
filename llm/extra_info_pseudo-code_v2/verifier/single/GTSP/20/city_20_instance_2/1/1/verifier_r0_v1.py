import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(cities, tour, total_cost, groups):
    # Check if tour starts and ends at the depot (city 0)
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the depot at start and end
        for idx, group in enumerate(groups):
            if city in group:
                visited_groups.add(idx)
                break
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Calculate the total travel cost from the given tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Compare the calculated cost to the provided total cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Cities coordinates (including depot as city 0)
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# City groups
groups = [[7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]]

# Provided solution details
tour = [0, 11, 16, 18, 19, 6, 0]
total_cost = 162.38

# Validate the solution
result = check_solution(cities, tour, total_cost, groups)
print(result)