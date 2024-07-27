import math

# Tour, total travel cost, and maximum distance from the proposed solution
solution_tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
solution_total_cost = 365.33
solution_max_distance = 61.68

# Coordinates of cities
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

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution_tour():
    # Check if the tour starts and ends at city 0
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"

    # Check if every city is visited exactly once excluding the depot city
    unique_cities = set(solution_tour[1:-1])
    if len(unique_cities) != 9 or sorted(unique_cities) != list(range(1, 10)):
        return "FAIL"

    # Verify distances and calculate total travel cost
    total_cost = 0
    local_max_distance = 0
    
    for i in range(len(solution_tour) - 1):
        distance = calculate_euclidean_distance(cities[solution_tour[i]], cities[solution_tour[i+1]])
        total_cost += distance
        local_max_distance = max(local_max_distance, distance)
    
    # Check the accuracy of total cost and max distance
    if not math.isclose(total_cost, solution_total_cost, rel_tol=1e-2) or \
       not math.isclose(local_max_distance, solution_max_distance, rel_tv=1e-2):  # Fixed the variable name here
        return "FAIL"
    
    return "CORRECT"

# Run test
result = test_solution_tour()
print(result)