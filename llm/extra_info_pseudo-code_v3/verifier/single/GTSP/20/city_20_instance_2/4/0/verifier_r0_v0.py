import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour():
    cities = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
        (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
        (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
    ]
    groups = [
        [7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]
    ]
    
    tour = [0, 11, 16, 18, 19, 6, 0]  # Given solution
    reported_cost = 162.3829840233368  # Given distance
    
    # Check if starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the depot from both ends for this verification
        for index, group in enumerate(groups):
            if city in group:
                visited_groups.add(index)
                break
    if len(visited_groups) != 5:
        return "FAIL"
    
    # Check if total travel cost is correct
    calculated_distance = 0
    for i in range(len(tour) - 1):
        calculated_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_distance, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Running the verification
print(verify_tour())