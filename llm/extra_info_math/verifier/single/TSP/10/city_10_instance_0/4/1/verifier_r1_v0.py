import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour_and_cost(tour, cities, total_travel_cost):
    # [Requirement 1] Check if start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once, except depot
    visited = set(tour)
    if len(tour) - 1 != len(cities) or len(visited) != len(cities):
        return "FAIL"
    
    # calculate the tour cost and compare with provided total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # [Requirement 4] Check if the calculated cost matches the total travel cost given
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = {
    0: (50, 42),  # Depot
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

# Solution provided
tour = [0, 5, 9, 8, 3, 4, 1, 2, 6, 7, 0]
total_travel_cost = 244.42473845

# Verify the solution
result = verify_tour_and_cost(tour, cities, total_travel_cost)
print(result)