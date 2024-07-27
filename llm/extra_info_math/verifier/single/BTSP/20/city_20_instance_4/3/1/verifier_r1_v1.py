import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, max_distance_consecutive_cities):
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    if len(set(tour)) != len(cities) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    calculated_total_cost = 0
    calculated_max_distance = 0

    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance_consecutive_cities, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 13, 18, 1, 11, 5, 14, 9, 7, 3, 4, 10, 16, 2, 12, 6, 15, 8, 19, 17, 0]
total_travel_cost = 654.9477933852553
max_distance_consecutive_cities = 55.036351623268054

# Validate the solution
result = verify_solution(tour, total_travel_cost, max_distance_consecutive_cities)
print(result)  # should output "CORRECT" or "FAIL" based on whether the solution meets the requirements