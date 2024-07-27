import math

# Provided tour and total cost
tour = [0, 10, 0, 10, 0, 10, 0, 10, 0]
provided_total_cost = 85.04116650187721

# Cities with their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62), 
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Groups of cities
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def check_start_end(tour):
    """ Check if the robot starts and ends at the depot city 0. """
    return tour[0] == 0 and tour[-1] == 0

def check_visit_one_per_group(tour, city_groups):
    """ Check if exactly one city from each group is visited. """
    visited = set(tour)
    for group in city_groups:
        if sum((city in visited) for city in group) != 1:
            return False
    return True

def calculate_total_travel_cost(tour):
    """ Calculate the total travel cost for the tour. """
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

def verify_solution(tour, provided_total_cost, city_groups):
    """ Verify the robot's tour plan against the given requirements. """
    if not check_start_end(tour):
        return "FAIL - Tour doesn't start and end at depot"
    
    if not check_visit_one_per_group(tour, city_groups):
        return "FAIL - Tour doesn't visit exactly one from each city group"
    
    calculated_cost = calculate_total_travel_cost(tour)
    if abs(calculated_cost - provided_total_cost) > 1e-6:
        return f"FAIL - Provided cost: {provided_total_cost}, Calculated cost: {calculated_cost}"
    
    return "CORRECT"

# Run the verification and print the result
result = verify_solution(tour, provided_total_cost, city_groups)
print(result)