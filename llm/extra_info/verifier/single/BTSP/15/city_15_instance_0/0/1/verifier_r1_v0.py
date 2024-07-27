import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def validate_tsp_solution(tour, city_positions, expected_total_cost, expected_max_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Start or end city is not the depot
    
    if sorted(tour) != sorted(list(set(tour))):
        return "FAIL"  # Some cities are visited more than once or missing
    
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist

    if round(calculated_total_cost, 2) != expected_total_cost:
        return "FAIL"  # Total travel cost does not match
    
    if calculated_max_distance != expected_max unst_distance:
        return "FAIL"  # Max distance between consecutive cities does not match
    
    return "CORRECT"

# Input data
city_positions = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}
tour = [0, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
expected_total_cost = 0
expected_max_distance = 0

# Test the solution
result = validate_tsp_solution(tour, city_positions, expected_total_cost, expected_max_distance)
print(result)