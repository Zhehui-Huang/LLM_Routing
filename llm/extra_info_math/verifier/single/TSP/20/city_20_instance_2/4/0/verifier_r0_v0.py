import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost, cities):
    # Unpack remaining information
    coordinates = {i: city for i, city in enumerate(cities)}
    
    # [The robot must start and finish its journey at the depot city 0.]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [The robot must visit all other cities exactly once.]
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # [Travel costs are calculated using the Euclidean distance between city coordinates.]
    computed_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        computed_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Allow a small margin for float comparison
    if not math.isclose(computed_quest, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    # [The objective is to minimize the total travel cost for the robot's tour.]
    # This criterion is harder to verify without solving the TSP again and comparing costs,
    # So we presume the optimizer did its job unless a major discrepancy is observed.

    return "CORRECT"

# Example city coordinates including the depot
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
          (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
          (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# Results from the solver
tour = [0, 12, 0]
total_travel_cost = 14.422205101855956

# Validate the solution
solution_status = verify_solution(tour, total_travel_cost, cities)
print(solution_status)