import math

# City coordinates corresponding to each city index
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Group information
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Create a function to calculate the Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Proposed solution tour and cost
proposed_tour = [0, 10, 1, 9, 0]
proposed_cost = 122.21527940040238

# Test function to check the validity of the proposed tour
def test_tour_and_cost(tour, cost):
    # Verify tour starts and ends at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0 :
        return "FAIL"
    
    # Verify each group has exactly one city visited
    visited_groups = {0: [], 1: [], 2: []}
    for city in tour[1:-1]:
        for group, cities in groups.items():
            if city in cities:
                visited_groups[group].append(city)
                break
    
    if any(len(cities) != 1 for cities in visited_groups.values()):
        return "FAIL"
    
    # Verify total cost calculation
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_cost, cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks passed, return "CORRECT"
    return "CORRECT"

# Run the test function
result = test_tour_and_cost(proposed_tour, proposed_cost)
print(result)