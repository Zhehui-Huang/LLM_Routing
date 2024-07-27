import numpy as np

def calculate_euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_tours_and_costs(tours, costs, cities):
    all_visited = set()
    total_calculated_cost = 0.0
    
    for i, tour in enumerate(tours):
        previous_city = tour[0]
        travel_cost = 0.0
        for city in tour[1:]:
            travel_cost += calculate_euclidean_distance(cities[previous_city], cities[city])
            previous_city = city
        total_calculated_cost += travel_cost
        all_visited.update(tour)
        
        # Check if the reported cost matches the calculated cost
        if not np.isclose(travel_cost, costs[i], atol=1e-2):
            return False
    
    # Checking if all cities are visited exactly once and all tours start at depot 0
    if all_visited == set(range(22)) and all(tour[0] == 0 for tour in tours):
        if np.isclose(total_calculated_cost, sum(costs), atol=1e-2):
            return True
    
    return False

# City coordinates including depots
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]

# Tours and costs provided in the solution
tours = [
    [0, 1, 2, 5, 7, 9, 10, 8, 6, 3, 4, 11],
    [0, 17, 20, 18, 0],
    [0, 12, 15, 14, 16, 13, 0],
    [0, 19, 21, 0]
]
costs = [109.3368914979458, 23.35530307777706, 61.029304375281704, 12.206555615733702]

# Verification
if verify_tours_and_costs(tours, costs, cities):
    print("CORRECT")
else:
    print("FAIL")