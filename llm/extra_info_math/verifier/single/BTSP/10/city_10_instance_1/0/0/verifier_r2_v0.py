import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def validate_tour(tour, coords):
    if tour[0] != tour[-1] or tour[0] != 0:
        return False, "Tour must start and end at the depot city 0"
    
    if len(set(tour) - {0}) != len(coords) - 1:
        return False, "Robot must visit each city exactly once"

    return True, ""

def calculate_total_cost(tour, coords):
    total_cost = 0
    distances = []
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coords[tour[i]], coords[tour[i+1]])
        distances.append(dist)
        total_cost += dist
    max_distance = max(distances)
    return total_cost, max_distance

# City coordinates including the depot
city_coords = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Solution
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
proposed_total_cost = 291.41088704894975
proposed_max_distance = 56.61271941887264

# Validators and Calculators
validity, message = validate_tour(tour, city_coords)
if not validity:
    print("FAIL")
else:
    total_cost, max_distance = calculate_total_cost(tour, city_coords)
    if abs(total_cost - proposed_total_cost) > 0.001 or abs(max_distance - proposed_max_distance) > 0.001:
        print("FAIL")
    else:
        print("CORRECT")