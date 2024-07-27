import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = {
        0: (16, 90), 
        1: (43, 99), 
        2: (80, 21), 
        3: (86, 92), 
        4: (54, 93),
        5: (34, 73), 
        6: (6, 61), 
        7: (86, 69), 
        8: (30, 50), 
        9: (35, 73), 
        10: (42, 64), 
        11: (64, 30), 
        12: (70, 95), 
        13: (29, 64), 
        14: (32, 79)
    }
    
    city_groups = [
        [1, 6, 14],
        [5, 12, 13],
        [7, 10],
        [4, 11],
        [2, 8],
        [3, 9]
    ]
    
    tour = [0, 14, 5, 10, 4, 8, 9, 0]
    reported_cost = 167.44393855985118
    
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour visits one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the depot city (start and end)
        for index, group in enumerate(city_group):
            if city in group:
                visited_groups.add(index)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Calculate the total travel distance
    distance = 0
    for i in range(len(tour) - 1):
        distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the calculated distance is approximately equal to the reported distance
    if not math.isclose(distance, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    # All tests passed
    return "CORRECT"

print(test_solution())