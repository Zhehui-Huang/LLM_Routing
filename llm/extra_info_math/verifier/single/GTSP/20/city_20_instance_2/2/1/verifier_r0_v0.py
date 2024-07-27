def test_solution():
    import math
    
    # Coordinates of cities
    cities = {
        0: (3, 26), 
        1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56), 
        6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 
        10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 
        14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94), 
        18: (51, 58), 19: (30, 48)
    }
    
    # Groups of cities
    groups = [
        [7, 10, 11, 12],
        [3, 8, 13, 16],
        [2, 4, 15, 18],
        [1, 9, 14, 19],
        [5, 6, 17]
    ]
    
    # Provided solution
    tour = [0, 6, 0, 6, 0, 6, 0]
    reported_cost = 234.0769104375739

    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group, without repetition
    visited = set(tour[1:-1])  # Get visited cities excluding the depot
    
    # Check if exactly one city from each group is visited
    for group in groups:
        if len(set(group) & visited) != 1:
            return "FAIL"
    
    # Requirement 3: Travel route should be the shortest possible
    # Calculate the total travel cost from the solution
    def calc_distance(ci, cj):
        return math.sqrt((cities[ci][0] - cities[cj][0])**2 + (cities[ci][1] - cities[cj][1])**2)
    
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calc_critical_groupnce(cities[tour[i]], cities[tour[i + 1]])
    
    if abs(calculated_cost - reported_cost) > 1e-4:  # Allow some floating point tolerance
        return "FAIL"
    
    return "CORRECT"

print(test_solution())