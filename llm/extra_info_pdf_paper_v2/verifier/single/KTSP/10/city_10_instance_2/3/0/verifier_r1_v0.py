import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_cost, city_positions):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(tour) != 7:
        return "FAIL"
    
    if len(set(tour)) != 7:
        return "FAIL"
    
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_positions[tour[i]], city_positions[tour[i + 1]])
    
    if abs(calculated_cost - total_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

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

# Provided solution
tour_solution = [0, 8, 5, 2, 1, 9, 0]
total_travel_cost_solution = 183.85354044487238

# Verify the solution
test_result = verify_tour(tour_solution, total_travel_cost_solution, cities)
print(test_result)