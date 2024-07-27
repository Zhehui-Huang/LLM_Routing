import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour, total_travel_cost):
    # City coordinates
    cities = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }
    
    # [The robot starts and ends its tour at depot city 0.]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [The robot needs to visit exactly 6 cities, including the depot city.]
    if len(tour) != 7:  # including the return to the origin
        return "FAIL"

    # Check for uniqueness and inclusion of cities 
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != 5 or 0 in visited_cities:
        return "FAIL"

    # [Travel cost between any two cities is calculated using the Euclidean distance.]
    # [The goal is to find the shortest possible tour that visits 6 cities.]
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    if not math.isclose(calculated_cost, total_travel_statistic, rel_tol=1e-4):
        return "FAIL"
    
    # [The solution output should be formatted as a list of city indices starting and ending at city 0, followed by the total travel cost of the tour.]
    # This part is more about the output formatting and is assumed correct by input.

    return "CORRECT"

# Provided solution
tour = [0, 6, 2, 1, 9, 0]
total_travel_cost = 274.7

# Validate the provided solution
result = validate_tour(tour, total_travel_cost)
print(result)