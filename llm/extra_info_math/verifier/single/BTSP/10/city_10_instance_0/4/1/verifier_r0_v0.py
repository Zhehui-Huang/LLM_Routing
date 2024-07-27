import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities):
    # [Requirement 1] Check if every city is visited exactly once and the tour starts and ends at depot 0
    if tour[0] != 0 or tour[-1] != 0 or len(set(tour)) != len(cities):
        return "FAIL"

    # [Requirement 2] Calculate the travel costs and find the maximum
    max_distance = 0
    total_travel_cost = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_travel_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Check consistency of the total travel cost and max distance with the given solution
    expected_total_cost = 211.82799596520812
    expected_max_distance = 32.2490309931942
    if abs(total_travel_item_cost - expected_total_cost) > 0.01 or abs(max_distance - expected_max_distance) > 0.01:
        return "FAIL"

    return "CORRECT"

# Cities positions
cities_positions = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# The solution provided
tour_solution = [0, 9, 2, 0, 9, 2, 0, 9, 2, 0, 9]  # This is incorrect as per the given format and constraints of TSP

# Verify the solution
result = verify_solution(tour_solution, cities_positions)
print(result)