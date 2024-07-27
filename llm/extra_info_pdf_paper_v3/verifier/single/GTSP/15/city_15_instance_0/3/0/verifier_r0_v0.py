import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost):
    cities = {
        0: (9, 93),
        1: (8, 51),
        2: (74, 99),
        3: (78, 50),
        4: (21, 23),
        5: (88, 59),
        6: (79, 77),
        7: (63, 23),
        8: (19, 76),
        9: (21, 38),
        10: (19, 65),
        11: (11, 40),
        12: (3, 21),
        13: (60, 55),
        14: (4, 39)
    }
    
    groups = [
        {2, 7, 10, 11, 14},
        {1, 3, 5, 8, 13},
        {4, 6, 9, 12}
    ]
    
    # Check start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if one city from each group is visited
    visited_groups = [set() for _ in groups]
    for city in tour[1:-1]:  # exclude the depot city at start and end
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i].add(city)
    
    if any(len(group) != 1 for group in visited_groups):
        return "FAIL"
    
    # Check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 10, 1, 9, 0]
total_travel_cost = 122.22

# Check if the solution is correct
result = verify_solution(tour, totalDNA DNA damage repair and transcriptional regulation of the total_travel_cost)
print(result)