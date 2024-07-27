import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    # Provided cities coordinates
    cities = [
        (90, 3),   # City 0: Depot
        (11, 17),  # City 1
        (7, 27),   # City 2
        (95, 81),  # City 3
        (41, 54),  # City 4
        (31, 35),  # City 5
        (23, 95),  # City 6
        (20, 56),  # City 7
        (49, 29),  # City 8
        (13, 17)   # City 9
    ]

    # Solution provided
    tour = [0, 3, 6, 4, 7, 2, 1, 9, 5, 8, 0]
    reported_cost = 354.91
    
    # Check if the tour begins and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour includes all cities exactly once, except the depot which should appear twice
    if sorted(tour) != [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return "FAIL"
    
    # Calculate the total tour cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check the calculated cost against the reported cost
    if abs(total_cost - reported_cost) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Execute the test function
result = test_solution()
print(result)