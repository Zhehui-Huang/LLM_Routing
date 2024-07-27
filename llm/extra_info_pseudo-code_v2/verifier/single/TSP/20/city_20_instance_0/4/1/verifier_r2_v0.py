import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_travel_cost(cities, tour):
    total_cost = 0
    for i in range(1, len(tour)):
        city1 = cities[tour[i-1]]
        city2 = cities[tour[i]]
        total_cost += euclidean_distance(city1, city2)
    return total_cost

def validate_tour(tour, num_cities, expected_total_cost, cities):
    # Requirement 2: Tour must start and end at the depot city, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Requirement 3: Robot must visit all cities exactly once, except the depot city
    if sorted(tour[1:-1]) != list(range(1, num_cities)):
        return False

    # Requirement 6: Output should be the tour starting and ending at city 0
    # Requirement 7: Check the reported total cost matches the calculated
    if not math.isclose(expected_total_cost, total_travel_cost(cities, tour), rel_tol=1e-7):
        return False

    return True

def test_tour():
    cities = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
        (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
        (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]
    proposed_tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
    proposed_total_cost = 349.1974047195548

    if validate_tour(proposed_tour, len(cities), proposed_total_cost, cities):
        return "CORRECT"
    else:
        return "FAIL"

print(test_tour())