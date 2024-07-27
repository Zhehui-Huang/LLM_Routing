import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def test_solution():
    cities_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35), 21: (32, 39), 22: (56, 37)
    }
    # Optimal tour provided:
    optimal_tour = [0, 2, 3, 20, 0, 6, 22, 5, 13, 1, 4, 21, 16, 10, 15, 11, 9, 8, 18, 14, 19, 12, 7, 17]
    # Verify all cities are visited exactly once
    if sorted(optimal_tour[1:-1]) != sorted(list(cities_coordinates.keys())):
        print("FAIL: Not all cities are visited exactly once.")
        return
    
    if optimal_tour[0] != 0 or len(set(optimal_tour))-1 != len(optimal_tour)-1: 
        print("FAIL: Tour should start and end at city 0, and cities should not repeat.")
        return

    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(optimal_tour)-1):
        total_cost += calculate_distance(cities_coordinates[optimal_tour[i]], cities_coordinates[optimal_tour[i+1]])
    
    # Expected total cost
    expected_total_cost = 434.9984610843018
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-6):
        print(f"FAIL: Calculated total cost {total_cost} does not match expected {expected_total_cost}.")
        return
    
    print("CORRECT")

test_solution()