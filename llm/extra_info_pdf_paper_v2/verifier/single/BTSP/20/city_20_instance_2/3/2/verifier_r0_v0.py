import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour(tour, city_coordinates, total_travel_cost, max_distance):
    # Requirement 1: Start and finish at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited exactly once (except for the depot which is visited twice)
    unique_cities = set(tour)
    if len(tour) - 1 != len(city_coordinates) or len(unique_cities) != len(city_coordinates):
        return "FAIL"

    # Calculate total cost and max travel distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city1 = city_coordinates[tour[i]]
        city2 = city_coordinates[tour[i+1]]
        distance = calculate_euclidean_distance(city1, city2)
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Check total travel cost and max distance against provided values
    if abs(calculated_total_cost - total_travel_cost) > 1e-2 or abs(calculated_max_distance - max_distance) > 1e-2:
        return "FAIL"

    return "CORRECT"

# Providing the coordinates for cities
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
}

# Tour information provided
tour = [0, 6, 3, 1, 4, 8, 7, 5, 2, 9, 0]
total_travel_cost = 457.37
max_distance = 60.93

# Test the tour
result = test_tour(tour, [cities[i] for i in range(len(cities))], total_travel_cost, max_distance)
print(result)