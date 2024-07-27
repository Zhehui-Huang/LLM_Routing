import math

# Define the cities and their coordinates
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

# Define the groups
groups = {
    0: [1, 4],
    1: [2, 6],
    2: [7],
    3: [5],
    4: [9],
    5: [8],
    6: [3]
}

# Proposed tour and cost provided by the solver
proposed_tour = [0, 3, 0, 0]
proposed_cost = 35.608987629529715

def calculate_euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def check_requirements(tour, groups, cities, proposed_cost):
    # Requirement 1: Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited = set(tour[1:-1])  # Ignore the first and last elements (depot)
    for group in groups.values():
        if not (visited & set(group)):
            return "FAIL"  # No city from this group is visited
    
    # Requirement 3: Check total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        p1 = cities[tour[i]]
        p2 = cities[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(p1, p2)
    
    if not math.isclose(calculated_cost, proposed_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run the test
result = check_requirements(proposed_tour, groups, cities, proposed_cost)
print(result)