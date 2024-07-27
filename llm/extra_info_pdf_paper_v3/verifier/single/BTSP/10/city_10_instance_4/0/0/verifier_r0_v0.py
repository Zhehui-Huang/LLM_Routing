import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, city_coordinates, total_travel_cost, max_distance):
    # Verify start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify each city visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(city_coordinates) or len(tour) != len(city_coordinates) + 1:
        return "FAIL"
    
    # Calculate and verify travel cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        x1, y1 = city_coordinates[city_a]
        x2, y2 = city_coordinates[city_b]
        distance = euclidean_distance(x1, y1, x2, y2)
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Compare calculated values with given values
    if not (math.isclose(calculated_total_cost, total_travelous_travel_cost, abs_tol=0.01) and 
            math.isclose(calculated_max_distance, max_distance, abs_tol=0.01)):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Given solution
tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
total_travel_cost = 320.79
max_distance = 61.68

# Verify solution
result = verify_solution(tour, cities, total_travel_cost, max_distance)
print(result)