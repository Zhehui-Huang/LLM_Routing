import math

def calculate_distance(city1, city2):
    """ Helper function to calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities, total_travel_cost, tour_output):
    """ Function to verify the given requirements. """
    if not tour or not cities or total_travel_cost is None:
        return "FAIL"
    
    # Requirement 1: Start and end at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Tour must include exactly 10 cities
    if len(tour) != 11:  # includes the returning to depot city
        return "FAIL"
    
    # Requirement 4: Output should include both the tour as a list of city indices starting and ending at the depot
    # and the total cost of the tour.
    if tour_output['Tour'] != tour or tour_output['Total travel cost'] != total_travel_cost:
        return "FAIL"
    
    # Check if all cities in the tour except the last (return to depot) are unique and total 10 cities considered
    unique_cities = set(tour[:-1])
    if len(unique_cities) != 10:
        return "FAIL"
    
    # Calculate the total distance of the given tour and compare with provided total_travel_cost
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Example test inputs
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Simulated output from the solution. Assuming this is the output from the algorithm.
output = {
    'Tour': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    'Total travel cost': 400.0
}

print(verify_tour(output['Tour'], cities, output['Total travel cost'], output))