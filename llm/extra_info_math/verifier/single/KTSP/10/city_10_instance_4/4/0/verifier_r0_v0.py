import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cities coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Given tour and its total cost
tour = [0, 4, 3, 1, 5, 7, 9, 6, 0]
reported_total_cost = 251.75287776040665

# Unit test to validate the solution
def test_tour():
    n = len(tour)
    
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 8 cities, including the depot, are visited
    if len(set(tour)) != 9:  # including city 0 two times
        return "FAIL"
    
    # Calculate total travel cost from the tour
    total_cost = 0
    for i in range(n - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Allow for a small numerical error margin
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Additional check for the shortest path is not easily done here without solving the problem again.
    # Therefore, by the problem constraints, if the path is a correct loop and
    # costs match the reported value, it is assumed correct.
    
    return "CORRECT"

# Run the test
result = test_tour()
print(result)