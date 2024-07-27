import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_gtspt_solution():
    # City coordinates
    cities = {
        0: (84, 67), # Depot
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # City groups
    city_groups = [
        [7, 9],
        [1, 3],
        [4, 6],
        [8],
        [5],
        [2]
    ]
    
    # Proposed tour and travel cost
    tour = [0, 7, 1, 4, 8, 5, 2, 0]
    reported_cost = 324.18
    
    # Check Requirement 1: Tour starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL")
        return "FAIL"
    
    # Check Requirement 4: Validate all cities are in the tour
    if len(cities) != 10 or any(city not in cities for city in tour):
        print("FAIL")
        return "FAIL"
    
    # Check Requirement 2: Exactly one city from each group
    visited_groups = []
    for city in tour:
        for i, group in enumerate(city_groups):
            if city in group and i not in visited_groups:
                visited_groups.append(i)
                break
    if len(visited_groups) != len(city_groups):
        print("FAIL")
        return "FAIL"
    
    # Check Requirement 3 and 5: Correct tour distance calculation
    total_distance_calculated = 0
    for i in range(len(tour) - 1):
        total_distance_calculated += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_distance_calculated, reported_cost, abs_tol=0.01):
        print(f"FAIL: Calculated distance {total_distance_calculated} does not match reported {reported_cost}")
        return "FAIL"

    print("CORRECT")
    return "CORRECT"

test_gtspt_solution()