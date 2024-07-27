import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, costs, total_cost):
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
        (45, 35), (32, 39), (56, 37)
    ]
    
    all_cities_visited = set()
    calculated_total_cost = 0
    
    # Check each robot
    for i, tour in enumerate(tours):
        # Check if the tour starts and ends at the same depot
        if tour[0] != tour[-1]:
            return "FAIL"
        start_end = tour[0]
        if i != start_end:  # Check if robot starts and ends at its assigned depot
            return "FAIL"
        
        travel_cost = 0
        for j in range(1, len(tour)):
            city_a_index = tour[j - 1]
            city_b_index = tour[j]
            city_a = coordinates[city_a_index]
            city_b = coordinates[city_b_index]
            travel_cost += calculate_distance(city_a, city_b)
            all_cities_visited.add(city_a_index)
            all_cities_visited.add(city_b_index)
        
        # Check if the costs are properly calculated and rounded
        if round(travel_cost, 2) != costs[i]:
            return "FAIL"
        
        calculated_total_cost += travel_cost
    
    # Ensure all cities are visited exactly once
    if len(all_cities_visited) != len(coordinates):
        return "FAIL"
    
    # Check total costs to see if they are within acceptable rounding error range
    if not math.isclose(calculated_total_cost, total_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Provided tours and their costs
tours = [
    [0, 21, 0], [1, 15, 1], [2, 10, 2], [3, 8, 18, 19, 12, 3],
    [4, 11, 4], [5, 14, 17, 9, 13, 22, 5], [6, 16, 6], [7, 20, 7]
]
costs = [4.47, 34.00, 21.26, 50.55, 14.42, 48.30, 12.81, 18.44]
total_cost = 204.25

# Execute the verification function with corrected values and variable names
print(verify_solution(tours, costs, total_cost))