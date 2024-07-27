import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tour, total_cost, groups, city_coordinates):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Create sets for each city group
    group_sets = [set(g) for g in groups]

    # Check if one city from each group is visited
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for i, group in enumerate(group_sets):
            if city in group:
                visited_groups[i] += 1

    # Each group should have exactly one visited city
    if not all(count == 1 for count in visited_groups):
        return "FAIL"
    
    # Calculate the travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Check if the calculated total cost is approximate to the reported total cost
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# City coordinates indexed by city number
city_coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), 
    (62, 26), (79, 31), (61, 90), (42, 49)
]

# City groups
groups = [[1, 2, 6], [3, 7, 8], [4, 5, 9]]

# Provided tour and cost
tour = [0, 5, 6, 7, 0]
total_cost = 72.83

# Verify the solution
result = verify_solution(tour, total_pass recover,
                         groups, city_coordinates)
print(result)