import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # Define city coordinates
    cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

    # City groups
    city_groups = [[1, 2, 6], [3, 7, 8], [4, 5, 9]]

    # Check Requirement 1: Visit exactly one city from each group
    visited_groups = [0] * len(city_groups)
    for city_index in tour[1:-1]:  # Exclude the depot city from checking groups
        for group_index, group_cities in enumerate(city_groups):
            if city_index in group_cities:
                visited_groups[group_index] += 1

    if any(count != 1 for count in visited_groups):
        print("FAIL: Not exactly one city from each group is visited")
        return

    # Check Requirement 2: Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL: Tour does not start and end at the depot city")
        return

    # Check Requirement 4: Output format
    if not all(isinstance(i, int) for i in tour):
        print("FAIL: Tour format is incorrect, should be list of integers")
        return

    # Check Requirement 3 & 5: Travel cost calculated correctly
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(computed_cost, total_cost, rel_tol=1e-2):
        print("FAIL: Computed travel cost does not match the given total cost")
        return

    print("CORRECT")

# Provided solution
solution_tour = [0, 5, 6, 7, 0]
solution_total_cost = 72.83

verify_solution(solution_tour, solution_total_cost)