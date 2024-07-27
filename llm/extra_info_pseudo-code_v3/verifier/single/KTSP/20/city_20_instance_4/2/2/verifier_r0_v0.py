import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates):
    # Ensure the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Ensure exactly 16 cities are visited
    if len(tour) != 17:  # Includes start and end at the depot
        return "FAIL"
    
    # Verify unique visits and the presence of the depot city in the solution
    if len(set(tour)) != 17 or tour.count(0) != 2:
        return "FAIL"
    
    # Calculate the tour cost and check if it equals the given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1_idx, city2_idx = tour[i], tour[i + 1]
        city1, city2 = city_coordinates[city1_idx], city_coordinates[city2_idx]
        calculated_cost += euclidean_distance(city1, city2)
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

city_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

tour = [0, 15, 3, 6, 12, 7, 16, 5, 2, 14, 11, 13, 18, 17, 8, 19, 0]
total_travel_cost = 335.64778862094005

result = verify_solution(tour, total_travel_cost, city_coordinates)
print(result)