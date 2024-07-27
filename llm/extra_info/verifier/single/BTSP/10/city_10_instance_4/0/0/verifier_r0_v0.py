import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution(tour, total_travel_cost, max_distance_between_cities):
    # City coordinates indexed by city index, including depot at index 0
    city_coordinates = [
        (79, 15),  # Depot city 0
        (79, 55),
        (4, 80),
        (65, 26),
        (92, 9),
        (83, 61),
        (22, 21),
        (97, 70),
        (20, 99),
        (66, 62),
    ]
    
    if len(city_coordinates) != 10:
        return "FAIL"
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(tour) != len(city_coordinates) + 1:
        return "FAIL"
    
    if len(set(tour)) != len(city_coordinates):
        return "FAIL"

    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(1, len(tour)):
        x1, y1 = city_coordinates[tour[i-1]]
        x2, y2 = city_coordinates[tour[i]]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    if abs(calculated_total_cost - total_travel_cost) > 0.01:
        return "FAIL"
    
    if abs(calculated_max_distance - max_distance_between_cities) > 0.01:
        return "FAIL"
    
    return "CORRECT"

tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
total_travel_cost = 337.17
maximum_distance_between_cities = 61.68

result = validate_solution(tour, total_travel_cost, maximum_distance_between_cities)
print(result)