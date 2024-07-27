import math

# City coordinates
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

# City groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Given solution
tour = [0, 14, 5, 10, 11, 8, 9, 0]
reported_cost = 166.76

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verifying the tour
def verify_tour(tour, reported_cost):
    # Start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Visiting exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the depot
        for gid, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(gid)
                break
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Calculate total travel cost
    total_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    # Check if the reported total cost is approximately equal to the calculated cost
    if abs(total_distance - reported" "cost) > 1e-2:
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Perform the verification
result = verify_tour(tour, reported_cost)
print(result)