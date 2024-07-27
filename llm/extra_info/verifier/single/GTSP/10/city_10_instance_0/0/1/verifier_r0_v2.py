import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities with coordinates (x1, y1) and (x2, y2). """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, cities, groups):
    # Check starting and ending at the depot
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Collect visited city indices from tour
    visited_cities = set(tour[1:-1])  # Extract city indices, excluding the depot
    
    # Check if exactly one city from each group is visited
    visited_groups = [False] * len(groups)
    for i, group in enumerate(groups):
        group_intersect = visited_cities.intersection(group)
        if len(group_intersect) != 1:
            return "FAIL"
        visited_groups[i] = True
    
    # Confirm all groups are represented in tour
    if not all(visited_groups):
        return "FAIL"
    
    # Calculate total distance from the tour
    calculated_total_distance = 0
    for i in range(len(tour) - 1):
        calculated_total_distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check the reported distance matches calculated distance
    if not math.isclose(calculated_total_distance, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates: [x, y]
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

# City groups
groups = [
    [1, 2, 6],  # Group 0
    [3, 7, 8],  # Group 1
    [4, 5, 9]   # Group 2
]

# Input solution proposal
tour = [0, 6, 7, 5, 0]
total_travel_cost = 74.94753083872993

# Run the verification
result = verify_solution(tour, total_travel_cost, cities, groups)

print(result)