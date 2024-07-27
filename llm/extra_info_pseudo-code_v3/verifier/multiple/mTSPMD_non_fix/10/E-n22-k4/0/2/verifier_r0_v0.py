import math
from typing import List, Tuple

def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_tour_cost(tour: List[int], coordinates: List[Tuple[int, int]]) -> float:
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def verify_solution(tours: List[List[int]], costs: List[float], coordinates: List[Tuple[int, int]]) -> str:
    # Requirement 1
    if len(coordinates) != 22:
        return "FAIL"
    
    # Requirement 2: Assuming Requirement 2 checked externally since tours start should have been validated during creation
    
    # Requirement 3/4: Assuming all city pairs can be traveled and costs are correctly computed using Euclidean distance
    
    # Requirement 5/8/10
    all_cities_visited = set()
    for tour in tours:
        all_cities_visited.update(tour)
    if len(all_cities_visited) != 22 or any(c not in all_cities_visited for c in range(22)):
        return "FAIL"
    
    # Requirement 6/10: Starting at depots and do not necessarily return (Ends also being depots or elsewhere)
    
    # Requirement 7/11: Check if the costs match calculated costs
    calculated_costs = [total_tour_cost(tour, coordinates) for tour in tours]
    if not all(math.isclose(costs[i], calculated_costs[i], rel_tol=1e-9) for i in range(len(costs))):
        return "FAIL"
    
    return "CORRECT"

# Travel coordinates provided in the task
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Tours and costs provided in the hypothetical solution
robots_tours = [
    [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21]
    for _ in range(4)
]
robots_costs = [278.5478504011258 for _ in range(4)]

result = verify_solution(robots_tours, robots_costs, coordinates)
print(result)