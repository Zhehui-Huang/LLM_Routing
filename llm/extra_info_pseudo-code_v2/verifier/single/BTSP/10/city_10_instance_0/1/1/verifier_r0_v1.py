import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour(tour, coords):
    # Requirement 4: starting and ending at the depot (city with index 0)
    if not (tour[0] == 0 and tour[-1] == 0):
        return False

    # Requirement 1: visit each city exactly once except the depot which is visited twice
    if sorted(tour) != [0, 0] + list(range(1, len(coords))):
        return False

    return True

def calculate_total_and_max_distance(tour, coords):
    total_distance, max_distance = 0, 0
    for i in range(len(tour)-1):
        dist = calculate_euclidean_distance(coords[tour[i]][0], coords[tour[i]][1], coords[tour[i+1]][0], coords[tour[i+1]][1])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

# Given solution infomation
tour_given = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
total_travel_cost_given = 328.3966856465968
max_distance_given = 45.18849411078001

# Coordinates of the cities
coords = [
    (50, 42),  # City 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

if verify_tour(tour_given, coords):
    calculated_total, calculated_max_distance = calculate_total_and_max_distance(tour_given, coords)
    # Requirement 5: check total travel cost
    # Requirement 6: check max distance between consecutive cities
    if (abs(calculated_total - total_travel_param_given) < 1e-6 and 
        abs(calculated_max_distance - max_distance_given) < 1e-6):
        print("CORRECT")
    else:
        print("FAIL")
else:
    print("FAIL")