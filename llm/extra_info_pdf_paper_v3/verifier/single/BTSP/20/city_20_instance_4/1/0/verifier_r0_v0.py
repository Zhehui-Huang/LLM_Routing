import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_tour(tour, cities):
    # Requirement 4: Validate the tour starts and ends at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Requirement 1: Validate all cities are visited exactly once (except for depot which is visited twice)
    visited = set(tour)
    if len(visited) != len(cities) or visited != set(range(len(cities))):
        return False
    
    return True

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def calculate_max_consecutive_distance(tour, cities):
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        if dist > max_distance:
            max_distance = dist
    return max_distance

# Test Setup
cities = [
    (26, 60),   # 0
    (73, 84),   # 1
    (89, 36),   # 2
    (15, 0),    # 3
    (11, 10),   # 4
    (69, 22),   # 5
    (28, 11),   # 6
    (70, 2),    # 7
    (47, 50),   # 8
    (60, 29),   # 9
    (29, 26),   # 10
    (85, 68),   # 11
    (60, 1),    # 12
    (71, 73),   # 13
    (82, 47),   # 14
    (19, 25),   # 15
    (75, 9),    # 16
    (52, 54),   # 17
    (64, 72),   # 18
    (14, 89)    # 19
]

tour_solution = [0, 10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 1, 13, 18, 17, 8, 19, 0]
claimed_total_cost = 379.72475773064514
claimed_max_distance = 51.088159097779204

# Validation
if not check_tour(tour_solution, cities):
    print("FAIL: Invalid tour.")
else:
    real_total_cost = calculate_total_travel_cost(tour_solution, cities)
    real_max_distance = calculate_max_consecutive_distance(tour_solution, cities)

    # Requirement 5 and 6: Check the total cost and max distance
    if math.isclose(real_total_cost, claimed_total_cost, rel_tol=1e-9) and math.isclose(real_max_distance, claimed_max_distance, rel_tol=1e-9):
        print("CORRECT")
    else:
        print("FAIL: Incorrect cost or distances.")