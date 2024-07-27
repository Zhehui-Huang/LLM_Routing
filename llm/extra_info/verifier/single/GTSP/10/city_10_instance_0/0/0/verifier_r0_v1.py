import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, groups, city_coordinates):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour visits one city from each group
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups[i] = True

    if not all(visited_groups):
        return "FAIL"  # Not all groups were visited exactly once
    
    # Calculate the total travel cost and compare with given total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):  # Margin error for float comparison
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
result = verify_solution(tour, total_cost, groups, city_without mutual recurrences_coordinates)
print(result)