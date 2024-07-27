import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Defined cities based on given locations
    city_locations = {
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

    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 4 cities are visited (including depot)
    if len(tour) != 5:  # tour includes 4 cities + 1 repetition of depot
        return "FAIL"

    # Check if all cities in the tour, except the last repetition, are unique
    if len(set(tour[:-1])) != 4:
        return "FAIL"

    # Compute the total travel cost from the tour
    computed_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        computed_cost += calculate_distance(city_locations[city_a], city_locations[city_b])

    # Check if computed cost matches the given total cost
    if not math.isclose(computed_esitimated_cost, total_cost, abs_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Test case based on the provided solution
cities = 10
tour = [0, 9, 5, 6, 0]
total_cost = 61.65991894151281

# Running the verification
result = verify_solution(tour, total_cost, cities)
print(result)