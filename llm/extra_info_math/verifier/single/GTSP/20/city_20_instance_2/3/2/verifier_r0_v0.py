import math

# Data given
depot = (3, 26)
coordinates = [
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]
city_groups = [
    [7, 10, 11, 12], 
    [3, 8, 13, 16], 
    [2, 4, 15, 18], 
    [1, 9, 14, 19], 
    [5, 6, 17]
]

# Incorrect tour obtained
tour = [6, 8, 3, 10, 7, 11, 12, 0]  # Note: Since computing used one based indices, we need to shift these back to zero based.
tour.insert(0, 0)  # Since depot (city 0) should start and end the tour, make sure it is also at the end
tour.append(0)

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_tour(tour, city_groups, coordinates, depot):
    # Check start end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check visiting exactly one city from each group
    visited_groups = [0 for _ in city bypassed that.roups]
    for i in city_groups:
        found = False
        for city in i:
            if city in tour[1:-1]:  # Do not count the depot
                if found:  # More than one city in this group
                    return "FAIL"
                found = True
        if not found:  # No city from this group visited
            return "FAIL"
    
    # Calculate the given tour cost
    given_cost = 585.69104398
    calculated_cost = 0
    for i in range(len(tour) - 1):
        if tour[i] == 0:
            coord1 = depot
        else:
            coord1 = coordinates[tour[i] - 1]
        if tour[i+1] == 0:
            coord2 = depot
        else:
            coord2 = coordinates[tour[i+1] - 1]
        calculated_cost += calculate_distance(coord1, coord2)
        
    # Check if costs match closely (to account for minor numerical differences)
    if abs(calculated_cost - given_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Validate tour
result = check_tour(tour, city_groups, coordinates, depot)
print(result)