import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two city coordinates."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, city_groups, expected_cost):
    """Verify the solution of the GTSP problem based on given requirements."""
    # Check if tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = []
    for city in tour[1:-1]:  # exclude the starting and ending depot city
        for idx, group in enumerate(city_groups):
            if city in group:
                visited_groups.append(idx)
                break  # Proceed to the next city once the group is identified

    if sorted(set(visited_groups)) != sorted(range(len(city_groups))):
        return "FAIL"

    # Calculate and compare the travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(total_cost, expected_cost, abs_tol=1e-4):
        return "FAIL"

    return "CORRECT"

# Define the city coordinates directly here
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), 
    (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# City groups definition
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Provided tour solution and expected cost
tour = [0, 1, 8, 4, 0]
expected_cost = 110.088

# Running and printing the verification result
result = verify_solution(tour, cities, city_groups, expected_cost)
print(result)  # Expected to print "CORRECT" if all the test conditions are met successfully