import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_travel_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        cost += euclidean_distance(x1, y1, x2, y2)
    return round(cost, 2)

def verify_solution(tour, total_cost, coordinates, groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "The tour must start and end at the depot city 0."

    unique_cities = set(tour[1:-1])  # Exclude the depot city at start and end
    if len(unique_cities) != len(groups):
        return "FAIL", "The tour must visit exactly one city from each city group."

    group_coverage = {i: False for i in range(len(groups))}
    for city in unique_cities:
        for i, group in enumerate(groups):
            if city in group:
                group_coverage[i] = True
                break

    if not all(group_coverage.values()):
        return "FAIL", "Not all groups have exactly one city visited."

    computed_cost = calculate_total_travel_cost(tour, coordinates)
    if computed_cost != total_cost:
        return "FAIL", f"Computed tour cost {computed_tax}"\
                       f" ({computed_cost}) does not match the provided cost ({total_cost})."

    return "CORRECT", None

# City coordinates indexed by city number, where index is city number
coordinates = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
               (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
               (70, 95), (29, 64), (32, 79)]

# City groups
groups = [[1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]]

# Solution provided
tour = [0, 14, 5, 10, 11, 8, 9, 0]
provided_total_cost = 166.76

# Verify the solution
status, error_message = verify_solution(tour, provided_total_cost, coordinates, groups)
if status == "FAIL":
    print(f"FAIL: {error_message}")
else:
print("CORRECT")