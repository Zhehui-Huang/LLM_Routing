import math

# Data from the problem statement:
depot = (3, 26)
coordinates = [
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]
city_groups = [
    [7, 10, 11, 12],  # Group 0
    [3, 8, 13, 16],   # Group 1
    [2, 4, 15, 18],   # Group 2
    [1, 9, 14, 19],   # Group 3
    [5, 6, 17]        # Group 4
]

# Incorrect tour obtained
tour = [6, 8, 3, 10, 7, 11, 12, 0]  
# Add the depot (0) at the beginning and end of the tour list to complete the loop
tour.insert(0, 0)  
tour.append(0)

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_tour(tour, city_groups, coordinates, depot):
    # Check if starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = set()
    for i, group in enumerate(city_groups):
        group_visited = any(city in tour for city in group)
        if group_visited:
            visited_groups.add(i)
    if len(visited_groups) != 5:  # There are 5 groups
        return "FAIL"

    # Check the total travel cost in the provided solution
    calc_cost = 0
    for i in range(len(tour) - 1):
        if tour[i] == 0:
            start = depot
        else:
            start = coordinates[tour[i] - 1]
        
        if tour[i+1] == 0:
            end = depot
        else:
            end = coordinates[tour[i+1] - 1]

        calc_cost += calculate_distance(start, end)
    
    # Given tour cost from the problem solution
    given_cost = 585.69104398
    if abs(calc_cost - given_cost) > 1e-3:  # Using a small tolerance for floating point comparison
        return "FAIL"

    return "CORRECT"

# Running the unit test for verification
result = check_tour(tour, city_groups, coordinates, depot)
print(result)