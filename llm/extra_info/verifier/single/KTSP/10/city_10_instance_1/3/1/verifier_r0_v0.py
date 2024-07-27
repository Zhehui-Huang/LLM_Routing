import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, travel_cost):
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    # [Requirement 1] Check if start and end at depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # [Requirement 2] Check if the tour includes exactly 5 different cities
    if len(tour) != 6 or len(set(tour)) != 5:  # including city 0 twice
        return "FAIL"
    
    # [Requirement 3] Compute the total travel distance and check if it matches the given cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(computed_cost, travel_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Given example
tour = [0, 4, 8, 3, 5, 0]
total_travel_cost = 110.38

# Verify the solution
result = verify_tour(tour, total_travel_cot)
print(result)