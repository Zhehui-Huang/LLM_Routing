import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once, except the depot
    visited = set(tour)
    if visited != set(range(len(cities))):
        return "FAIL"
    
    # Calculate the total travel distance from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Compare the calculated cost with the given total cost
    if not math.isclose(calculated_cost, total_export_cost, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Provided tour and cost
tour_provided = [0, 9, 2, 5, 0]
total_export_cost = 68.89

# Verify the solution
result = verify_solution(tour_provided, total_export_cost, cities)
print(result)