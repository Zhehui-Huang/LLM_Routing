import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities, expected_total_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 8 cities are included in the tour including the depot city
    if len(set(tour)) != 8:
        return "FAIL"

    # Check if the total tour cost is calculated correctly
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_cost, expected_total_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = {
    0: (79, 15),
    4: (92, 9),
    7: (97, 70),
    1: (79, 55),
    5: (83, 61),
    9: (66, 62),
    6: (22, 21),
    3: (65, 26),
}

# Provided solution
tour = [0, 4, 7, 1, 5, 9, 6, 3, 0]
total_travel_cost = 244.43

# Verify the solution
result = verify_tour(tour, cities, total_travel_cost)
print(result)