import math

def euclidean_distance(point1, point2):
    """Calculates the Euclidean distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution(cities, city_groups, tour, reported_cost):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        found_group = False
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups[i] += 1
                found_group = True
        if not found_group or visited_groups.count(0) > 0:
            return "FAIL"
    if any(v != 1 for v in visited_groups):
        return "FAIL"
    
    # Calculate the total cost of the provided tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Compare the calculated cost with the reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Given cities and their coordinates
cities_coordinates = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Grouping of cities
city_groups = [[3, 6], [5, 8], [4, 9], [1, 7], [2]]

# Provided Solution tour and its cost
tour = [0, 3, 5, 9, 1, 2, 0]
reported_cost = 281.6

# Verify the solution
solution_status = verify_solution(cities_coordinates, city_groups, tour, reported_cost)
print(solution_status)