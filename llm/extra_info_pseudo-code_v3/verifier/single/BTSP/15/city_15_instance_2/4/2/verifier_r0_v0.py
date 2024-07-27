import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }
    total_computed_cost = 0
    computed_max_dist = 0
    
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    if sorted(tour) != sorted([i for i in range(15)] + [0]):
        return "FAIL"
    
    # Calculate the total distance and maximum consecutive distance
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_computed_cost += dist
        if dist > computed_max_dist:
            computed_max_dist = dist
            
    # Check if the provided maximum distance is correct
    if not math.isclose(computed_max_dist, max_distance, abs_tol=1e-9):
        return "FAIL"
    
    # Check if the provided total cost is correct
    if not math.isclose(total_computed_cost, total_cost, abs_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
total_travel_cost = 676.812946106938
maximum_distance = 86.55634003352961

# Verify the solution
print(verify_solution(tour, total_travel_cost, maximum_distance))