import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost):
    # City coordinates
    cities = {
        0: (90, 3),  # depot
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }
    
    # City groups
    groups = [
        {3, 6},
        {5, 8},
        {4, 9},
        {1, 7},
        {2}
    ]
    
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check only one city from each group
    visited_from_group = set()
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        in_group = False
        for index, group in enumerate(groups):
            if city in group:
                if index in visited_from_group:
                    return "FAIL"
                visited_from_stop = True
                visited_from_group.add(index)
                in_group = True
                break
        if not in_group:
            return "FAIL"
    
    if len(visited_from_group) != len(groups):
        return "FAIL"
    
    # Check direct travel between cities (implicitly verified by tour being a list of city indices allowing direct travel)
    
    # Calculate and check travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(computed_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 3, 5, 2, 1, 9, 0]
total_travel_cost = 273.3072642077373

# Verify the solution
print(verify_solution(tour, total_travel_cost))