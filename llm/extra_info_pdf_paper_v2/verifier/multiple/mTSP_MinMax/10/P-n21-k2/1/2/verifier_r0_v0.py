import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_tours(tours, city_coordinates, expected_costs):
    cities_covered = set()
    
    for tour_i, tour in enumerate(tours):
        # Check Requirement 2 (Start and end at the depot city)
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check cities in each tour (Requirement 3)
        for city in tour[1:-1]:  # Check deployed cities, excluding depot at the start and at the end
            if city in cities_covered:
                return "FAIL"
            cities_covered.add(city)
        
        # Check calculated travel cost matches with expected (Requirement 5 and 6)
        travel_cost = sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour)-1))
        if not math.isclose(travel_cost, expected_costs[tour_i], rel_tol=1e-5):
            return "FAIL"
        
    # Check all non-depot cities are covered exactly once (Requirement 3)
    if len(cities_covered) != len(city_coordinates) - 1:
        return "FAIL"
    
    return "CORRECT"

city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

tours = [
    [0, 4, 1, 16, 6, 20, 14, 9, 18, 2, 13, 0],
    [0, 5, 17, 7, 10, 11, 15, 12, 3, 19, 8, 0]
]

expected_costs = [161.9480201240023, 164.52166030274907]

result = validate_tours(tours, city_coordinates, expected_costs)
print(result)  # This should output "CORRECT" if everything is as expected.