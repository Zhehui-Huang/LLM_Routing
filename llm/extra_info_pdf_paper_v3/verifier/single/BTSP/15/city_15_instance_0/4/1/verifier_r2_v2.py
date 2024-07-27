import math

# Define the city coordinates
cities = [
    (9, 93),  # City 0 - Depot
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Provide the solution tour and calculated metrics
solution_tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
solution_total_cost = 373.97
solution_max_distance = 63.6

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour(tour, cities):
    # Tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # All cities are visited exactly once
    if len(set(tour)) != len(cities):
        return False
    
    # Check provided total travel cost and max distance
    distances = [calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1)]
    calculated_total_cost = sum(distances)
    calculated_max_distance = max(distances)

    if abs(calculated_total_cost - solution_total_cost) > 0.01:
        return False
    if abs(calculated_max to solution_max_distance) > 0.01:
        return False

    return True

# Execute validation
if validate_tour(solution_tour, cities):
    print("CORRECT")
else:
    print("FAIL")