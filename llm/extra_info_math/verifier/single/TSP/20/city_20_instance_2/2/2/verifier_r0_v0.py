import math

# Extracted tour and total travel cost
tour = [0, 12, 0, 0]
reported_cost = 14.42

# The city coordinates from the given problem
city_coordinates = [
    (3, 26),  # City 0 (Depot)
    (85, 72), # City 1
    (67, 0),  # City 2
    (50, 99), # City 3
    (61, 89), # City 4
    (91, 56), # City 5
    (2, 65),  # City 6
    (38, 68), # City 7
    (3, 92),  # City 8
    (59, 8),  # City 9
    (30, 88), # City 10
    (30, 53), # City 11
    (11, 14), # City 12
    (52, 49), # City 13
    (18, 49), # City 14
    (64, 41), # City 15
    (28, 49), # City 16
    (91, 94), # City 17
    (51, 58), # City 18
    (30, 48)  # City 19
]

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def total_travel_cost(tour, city_coordinates):
    total_cost = 0.0
    for i in range(1, len(tour)):
        total_cost += calculate_euclidean_distance(city_coordinates[tour[i-1]], city_coordinates[tour[i]])
    return total_cost

def verify_tour(tour, city_coordinates):
    # Start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    # All cities visited only once
    visited = set(tour[1:-1])
    if len(visited) != (len(city_coordinates) - 1):
        return False
    # Travel cost (Calculated vs Reported)
    calculated_cost = round(total_travel_cost(tour, city_coordinates), 2)
    if abs(calculated_cost - reported_cost) > 0.01:
        return False
    return True

# Validate the solution
if verify_tour(tour, city_coordinates):
    print("CORRECT")
else:
    print("FAIL")