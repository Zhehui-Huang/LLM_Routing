import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def test_solution(tour, total_cost):
    # Cities coordinates
    cities = {
        0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59), 
        6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 
        12: (3, 21), 13: (60, 55), 14: (4, 39)
    }
    
    # City groups
    groups = [set([2, 7, 10, 11, 14]), set([1, 3, 5, 8, 13]), set([4, 6, 9, 12])]
    
    # Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Visit exactly one city from each group
    visited_groups = [set() for _ in groups]
    for i, group in enumerate(groups):
        for city in tour[1:-1]:  # Exclude start/end city in the tour path
            if city in group:
                visited_groups[i].add(city)
    if not all(len(group) == 1 for group in visited_groups):
        return "FAIL"
    
    # Calculate the total travel cost using Euclidean distance
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 10, 1, 9, 0]
total_cost = 122.22

# Execute test
result = test_solution(tour, total_recommend_cost)
print(result)