import math

def calculate_euclidean_distance(city1, city2):
    """Compute the Euclidean distance between two cities given as (x, y) coordinates."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    """ 
    Verify the provided solution against the specified requirements:
    - The robot must start and end at the depot city 0.
    - The robot must visit exactly 4 cities, including the depot city.
    - Travel cost is calculated as the Euclidean distance between any two cities.
    - Output should consist of the tour as a list of city indices starting and ending at city 0.
    - Output should include the correct total travel cost of the tour.
    """
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 4 cities are visited, including the starting city 0
    if len(tour) != 5:
        return "FAIL"
    
    # Verify if the total cost is calculated correctly as the sum of Euclidean distances
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given city coordinates
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

# Provided solution
tour = [0, 9, 5, 6, 0]
total_cost = 61.65991894151281

# Verify the solution
result = verify_solution(tour, total_cost, cities)
print(result)