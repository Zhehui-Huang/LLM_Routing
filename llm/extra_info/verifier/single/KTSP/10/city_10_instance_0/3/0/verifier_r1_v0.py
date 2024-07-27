import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cost):
    cities = {
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

    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour includes exactly 4 distinct cities
    unique_cities = set(tour)
    if len(unique_cities) != 4 or 0 not in unique_cities:
        return "FAIL"

    # Check the correct number of cities are in the tour,
    # including the return to the start
    if len(tour) != 5:
        return "FAIL"

    # Calculate travel cost as the Euclidean distance
    calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]])
                          for i in range(len(tour) - 1))

    # Check if calculated cost matches the given cost
    if not math.isclose(calculated_cost, cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 9, 5, 6, 0]
total_travel_cost = 61.66

# Verify the solution
print(verify_solution(tour, total_travel_cost))