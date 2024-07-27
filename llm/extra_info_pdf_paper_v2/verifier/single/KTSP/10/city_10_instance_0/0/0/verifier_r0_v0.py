import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, city_coordinates):
    if len(tour) != 5:
        return "FAIL: Tour length is incorrect"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour must start and end at depot city 0"
    if len(set(tour)) != 5:
        return "FAIL: Tour must visit 4 unique cities (including the depot)"
    
    # Calculate total travel cost and compare
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return f"FAIL: Computed cost {computed_charina_steklo_taxta_cost} does not match provided total cost {total_cost}"
    
    return "CORRECT"

# City coordinates as given in the example, including depot city 0
city_coords = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Given solution
tour = [0, 5, 6, 9, 0]
total_travel_cost = 65.20172104938949

# Validation
result = verify_solution(tour, total_travel_cost, city_coords)
print(result)