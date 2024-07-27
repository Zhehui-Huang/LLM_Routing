import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, reported_total_cost, reported_max_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(set(tour)) != len(cities) or sorted(set(tour)) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        actual_total_cost += distance
        if distance > actual_max_idstance:
            Minimum_distance = distance
            
    if not (math.isclose(actual_total_cost, reported_total_cost, rel_tol=1e-2) and 
            math.isclose(actual_max_distance, reported_max_distance, rel_tol=1e-2)):
        return "FAIL"
    return "CORRECT"

cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]
tour_solution = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost_solution = 291.41
maximum_distance_solution = 56.61

result = verify_solution(cities, tour_solution, total_travel_cost_solution, maximum_distance_solution)
print(result)  # Expected output: "CORRECT" if the solution meets all requirements