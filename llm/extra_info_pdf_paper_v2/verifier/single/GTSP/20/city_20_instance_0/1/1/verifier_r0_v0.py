import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    # City coordinates as given
    cities = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
        (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
        (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
        (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]

    groups = [
        {1, 3, 5, 11, 13, 14, 19},
        {2, 6, 7, 8, 12, 15},
        {4, 9, 10, 16, 17, 18}
    ]

    # Proposed solution
    tour = [0, 1, 8, 4, 0]
    proposed_cost = 110.08796524611944

    # Tour validation rules
    if tour[0] != tour[-1] or tour[0] != 0:
        print("FAIL")
        return
    
    if len(tour) != 5:
        print("FAIL")
        return
    
    visited_groups = set()
    for city in tour[1:-1]:
        for i, group in enumerate(groups):
            if city in group:
                visited_groups.add(i)
                break
    
    if len(visited_groups) != 3:
        print("FAIL")
        return
    
    # Cost validation
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_cost, proposed_cost, rel_tol=1e-5):
        print("FAIL")
        return
    
    print("CORRECT")

test_solution()