import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_distance(tour, city_coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        total_distance += euclidean_distance(city_coordinates[city1][0], city_coordinates[city1][1], 
                                             city_coordinates[city2][0], city_coordinates[city2][1])
    return total_distance

def verify_solution(tour, total_cost, city_coordinates):
    if len(city_coordinates) != 10:
        return "FAIL: Wrong number of cities."
    if tour[0] != tour[-1] or tour[0] != 0:
        return "FAIL: Tour must start and end at the depot city 0."
    if len(set(tour)) != len(city_coordinates) or len(tour) != 11:
        return "FAIL: Tour does not visit all cities exactly once."
    calculated_cost = calculate_total_distance(tour, city_coordinates)
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL: Total travel cost incorrect. Expected approximately {}, got {}".format(calculated_cost, total_cost)
    return "CORRECT"

# City coordinates
city_coordinates = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Solution Provided
tour_provided = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
total_cost_provided = 295.99

# Verify the solution
result = verify_solution(tour_provided, total_cost_provided, city_coordinates)
print(result)