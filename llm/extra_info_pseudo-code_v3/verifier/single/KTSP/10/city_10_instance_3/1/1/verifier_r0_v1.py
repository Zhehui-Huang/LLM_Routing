import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, total_travel_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(set(tour)) != 7:
        return "FAIL"

    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    
    if abs(calculated_cost - total_travel_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Corrected solution given
tour_given = [0, 8, 3, 7, 1, 2, 4, 0]
total_travel_cost_given = 159.97188184793015

# Verify the solution
result = verify_solution(tour_given, total_travel_cost_given, cities)
print(result)