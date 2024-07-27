import math

# Define the coordinates of the cities including the depot
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Tours given in the solution
robot_tours = [
    [0, 1, 11, 3, 17, 9, 15, 13, 5, 7, 0],  # Robot 0
    [0, 6, 18, 2, 8, 16, 12, 14, 4, 10, 0]  # Robot 1
]

# Report travel costs provided
robot_costs_provided = [
    151.45152819213507,  # Robot 0
    119.61742387001291   # Robot 1
]

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_tour(tour, robot_costs):
    # Verify the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Calculate total travel cost and verify with provided
    calculated_cost = sum(calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    if not math.isclose(calculated_cost, robot_costs, rel_tol=1e-5):
        return False
    
    return True

def verify_all_cities_visited_once_excluding_depot(robot_tours):
    all_visited = set()
    for tour in robot_tours:
        all_visited.update(tour[1:-1])  # Exclude depot (start and end)
    return all_visited == set(range(1, 19))

def verify_solution(robot_tours, robot_costs_provided):
    all_checks_pass = True
    
    # Check if all tours start and end at depot, and costs are correct
    for tour, cost in zip(robot_tours, robot_costs_provided):
        if not verify_tour(tour, cost):
            all_checks_pass = False
    
    # Check if each city, except depot, is visited exactly once
    if not verify_all_cities_visited_once_excluding_depot(robot_tours):
        all_checks_pass = False
    
    # Check if the maximum cost matches the reported maximum cost
    max_cost = max(robot_costs_provided)
    if max_cost != max(robot_costs_provided):
        all_checks_pass = False
    
    return "CORRECT" if all_checks_pass else "FAIL"

# Call the verification function and print the result
print(verify_solution(robot_tours, robot_costs_provided))