import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def validate_tour_solution(tour, travel_costs):
    # City coordinates
    coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    n = len(coordinates)
    
    # Requirement 1: The robot must start and end at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot must visit all cities exactly once, except the depot city.
    if sorted(tour[1:-1]) != list(range(1, n)):
        return "FAIL"
    
    # Requirement 3: The travel cost is the Euclidean distance between two cities.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        calculated_cost += dist
    if not math.isclose(calculated_cost, travel_costs, rel_tol=1e-9):
        return "FAIL"
    
    # Add more requirements if necessary, assuming additional checks have been performed elsewhere,
    # like enforcing integer programming discretization and sub-tour prevention.
    
    return "CORRECT"

# From solver output
tour = [0, 10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 1, 13, 18, 17, 8, 19, 0]
total_travel_cost = 379.72475773064514

# Validate the solution
result = validate_tour_solution(tour, total_travel_cost)
print(result)