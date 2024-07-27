import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_tour(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_distance

def unit_tests():
    # Provided tour and total cost
    given_tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
    given_total_travel_cost = 132.1185774560832

    # City coordinates
    city_coordinates = [
        (54, 87), # Depot
        (21, 84),
        (69, 84),
        (53, 40),
        (54, 42),
        (36, 30),
        (52, 82),
        (93, 44),
        (21, 78),
        (68, 14),
        (51, 28),
        (44, 79),
        (56, 58),
        (72, 43),
        (6, 99)
    ]

    # Check Requirement 2: Starting and ending at depot
    if given_tour[0] != 0 or given_tour[-1] != 0:
        print("FAIL: Tour does not start and end at the depot city")
        return

    # Check Requirement 3: Visits exactly 8 cities (including repeated depot)
    if len(set(given_tour)) != 8:
        print("FAIL: Tour does not visit exactly 8 unique cities")
        return

    # Check Requirement 6: Correct total travel cost
    calculated_cost = check_tour(given_tour, city_coordinates)
    if not math.isclose(calculated_cost, given_total_travel_cost, abs_tol=0.1):
        print(f"FAIL: Calculated travel cost {calculated_cost} does not match the given {given_total_travel_cost}")
        return
    
    print("CORRECT")

unit_tests()