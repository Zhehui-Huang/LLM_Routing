import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, city_positions, groups):
    # Requirement 1: Starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Requirement 2: Visits exactly one city per group
    visited = {}
    for i, group in enumerate(groups):
        count = sum(city in tour for city in group)
        if count != 1:
            return False
        visited.update({city: i for city in group if city in tour})
    
    # Check if each city in the tour is from unique and exactly one of the allowed groups
    if len(set(visited.values())) != len(groups):
        return False

    # Requirement 3: The travel cost is given and should match caclulated travel cost
    correct_total_cost = 266.72  # Provided as the supposedly correct answer
    calculated_cost = sum(euclidean_distance(city_positions[tour[i]], city_positions[tour[i + 1]]) for i in range(len(tour) - 1))
    
    if abs(calculated_cost - correct total_cost) > 0.01:  # Allowing a minor rounding difference
        return False

    return True

# City positions
city_positions = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# City groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]

if validate_tour(tour, city_positions, groups):
    print("CORRECT")
else:
    print("FAIL")