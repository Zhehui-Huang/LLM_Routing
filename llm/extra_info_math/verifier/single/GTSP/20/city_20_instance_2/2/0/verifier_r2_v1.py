import math

# Given city coordinates including the depot
cities = [
    (3, 26),   # City 0: Depot
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Grouping of cities
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Proposed tour from the solution
tour = [0, 6, 11, 18, 19, 16, 0]
proposed_travel_cost = 529.61  # Given cost from the output

# Calculate the Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Verify the tour and calculate the travel cost
def verify_tour(tour, groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", 0  # Tour must start and end at the depot
    
    group_visit_check = [False] * len(groups)
    actual_travel_cost = 0
    last_city = tour[0]
    
    for city in tour[1:]:
        actual_travel_cost += euclidean_distance(cities[last_city], cities[city])
        
        # Check group visiting rules
        for i, group in enumerate(groups):
            if city in group:
                if group_visit_check[i]:
                    return "FAIL", 0  # City from the same group visited more than once
                group_visit_check[i] = True
                break  # Exit the loop after finding the city in a group
        
        last_city = city
    
    if not all(group_visit_check):
        return "FAIL", 0  # Not all groups are visited exactly once
    
    return "CORRECT", actual_travel_cost

# Function call to verify the tour
result, calculated_cost = verify_tour(tour, groups)
if result == "CORRECT" and abs(proposed_travel_cost - calculated_cost) < 1e-5:
    print("CORRECT")
else:
    print("FAIL")