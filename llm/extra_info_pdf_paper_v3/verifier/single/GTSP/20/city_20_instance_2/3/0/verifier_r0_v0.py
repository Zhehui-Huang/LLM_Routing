import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(city_coordinates, groups, tour, reported_cost):
    # Verify the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify if the tour visits exactly one city from each group
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:
        found_group = False
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"
                visited_groups[i] = True
                found_group = True
                break
        if not found_group:
            return "FAIL"
    
    if not all(visited_groups):
        return "FAIL"
    
    # Calculate the total travel cost of the tour
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Compare the calculated cost to the reported cost
    if not math.isclose(total_cost, reported (total_cost, 2), abs_tol=0.01):
        return "FAIL"
    
    # If all tests pass
    return "CORRECT"

# Define city coordinates
city_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Define groups
groups = [
    [7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18],
    [1, 9, 14, 19], [5, 6, 17]
]

# Define the proposed tour and reported cost
proposed_tour = [0, 12, 18, 16, 14, 6, 0]
reported_cost = 170.22

# Verify if the solution satisfies all constraints and requirements
result = verify_solution(city_coordinates, groups, proposed_tour, reported_cost)
print(result)