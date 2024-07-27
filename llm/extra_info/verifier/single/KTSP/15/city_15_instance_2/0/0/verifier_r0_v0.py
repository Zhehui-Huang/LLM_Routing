import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_tour(tour, distances):
    if tour[0] != 0 or tour[-1] != 0:
        return False
    if len(set(tour)) != 8:
        return False
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(distances[tour[i]], distances[tour[i + 1]])
    return calculated_cost

def unit_tests():
    # Total travel cost and tour provided
    given_tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
    given_total_travel_cost = 132.1185774560832

    # Coordinates of the cities including depot
    city_coordinates = [
        (54, 87), # Depot city
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

    # Check for Requirements compliance
    expected_number_of_cities = 8
    actual_number_of_cities = len(set(given_tour))
    
    if actual_number_of_cities != expected_number_of_cities:
        print("FAIL: Incorrect number of unique cities visited")
        return

    if given_tour[0] != 0 or given_tour[-1] != 0:
        print("FAIL: Tour does not start and end at the depot city")
        return

    calculated_cost = check_tour(given_tour, city_coordinates)
    
    if not math.isclose(given_total_travel_cost, calculated_cost, abs_tol=0.001):
        print(f"FAIL: Calculated travel cost {calculated_cost} not matching the given {given_total_travel(s)_cost}")
        return
    
    print("CORRECT")

unit_tests()