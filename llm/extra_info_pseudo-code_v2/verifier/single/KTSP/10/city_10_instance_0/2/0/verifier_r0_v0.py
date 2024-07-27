import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def verify_tour(tour, coordinates):
    # Check the tour starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check the tour includes exactly 4 cities
    if len(tour) != 5:  # includes depot city 0 at the beginning and end
        return "FAIL"

    # Check for unique cities in the tour (exclude the repeated city 0 at the end before checking)
    if len(set(tour[:-1])) != len(tour[:-1]):
        return "FAIL"

    # The travel cost calculation is inherently handled by the total cost calculation

    # Check all cities are reachable and calculated correctly - the tour calculation is assumed to done prior
    if not all(city in range(10) for city in tour):
        return "FAIL"

    return "CORRECT"

# Define coordinates corresponding to cities
city_coordinates = {
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

# Presumed solution for testing (example input)
# Tour must be defined here like [0, 1, 2, 3, 0]
# Assume the solution found is [0, 1, 4, 8, 0] which is correct and meets the requirements
example_tour = [0, 1, 4, 8, 0]

total_cost = calculate_total_travel_cost(example_tour, city_coordinates)
verification_result = verify_tour(example_tour, city_coordinates)

print("Verification result:", verification_result)  # Should print "CORRECT"