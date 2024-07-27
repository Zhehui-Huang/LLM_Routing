import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost, cities):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities (1 to 19) are visited exactly once
    visited = set(tour[1:-1])
    if len(visited) != 19 or any([city < 1 or city > 19 for city in visited]):
        return "FAIL"
    
    # Check the total travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_cost, calculated_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# City coordinates including depot
cities = [
    (26, 60),  # depot city 0
    (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26),
    (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Solution and travel cost provided
solution_tour = [0, 19, 0, 19, 0, 19, 0, 19, 0, 19, 0, 19, 0, 19, 0, 19, 0, 19, 0, 19, 0]
solution_cost = 627.69

# Run tests on the solution
result = verify_solution(solution_tour, solution_cost, cities)
print(result)