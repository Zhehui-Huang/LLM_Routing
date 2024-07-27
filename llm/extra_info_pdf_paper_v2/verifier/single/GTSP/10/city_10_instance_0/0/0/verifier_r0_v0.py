import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_cost(tour, coordinates):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += euclidean_path_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def check_tour(tour, total_cost, coordinates, groups):
    # Requirement 1: Start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city which might be at both start and end
        for index, group in enumerate(groups):
            if city in group:
                visited_groups.add(index)
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Requirement 3: Travel cost calculated with Euclidean distance
    calculated_cost = calculate_total_cost(tour, coordinates)
    if not math.isclose(total_cost, calculated_cost, abs_tol=0.01):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Unit Test
coordinates = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]
groups = [[1, 2, 6], [3, 7, 8], [4, 5, 9]]
tour = [0, 6, 7, 5, 0]
total_cost = 74.95

# Calling the check function
print(check_tour(tour, total_cost, coordinates, groups))