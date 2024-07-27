import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
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

# Output from the solver
tour = [0, 2, 4, 3, 8, 9, 5, 1, 6, 7, 0]
actual_total_cost = 302.18715914967925
actual_max_distance = 45.18849411078001

# Checks
# Check if the tour starts and ends at the depot
def check_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check if all cities are visited exactly once, except the depot which should be twice
def check_visits(tour):
    counts = {i: tour.count(i) for i in set(tour)}
    return all(count == 1 for i, count in counts.items() if i != 0) and counts[0] == 2

# Calculate and compare the total cost and maximum distance
def calculate_costs(tour, cities):
    distances = [euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1)]
    total_distance = sum(distances)
    max_distance = max(distances)
    return total_distance, max_distance

# Perform the unit tests
def unit_tests():
    total_cost, max_distance = calculate_costs(tour, cities)
  
    if (check_depot(tour) and check_visits(tour) and
        math.isclose(actual_total_cost, total_cost, rel_tol=1e-9) and
        math.isclose(actual_max_distance, max_distance, rel_tol=1e-9)):
        return "CORRECT"
    else:
        return "FAIL"

# Output the result of the tests
result = unit_tests()
print(result)