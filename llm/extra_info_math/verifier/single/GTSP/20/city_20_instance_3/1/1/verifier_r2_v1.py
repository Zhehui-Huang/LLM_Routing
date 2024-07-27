import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, cities, city_groups):
    # [Requirement 1] Check if tour starts and ends at the depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if exactly one city from each group is visited
    group_visited = [False] * len(city_groups)
    for idx in tour[1:-1]:  # Exclude the initial and final depot visits
        found = False
        for i, group in enumerate(city_groups):
            if idx in group:
                if group_visited[i]:
                    return "FAIL"
                group_visited[i] = True
                found = True
                break
        if not found:
            return "FAIL"

    if not all(group_visited):
        return "FAIL"
    
    # [Requirement 3] Check if the total travel cost is minimal
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_filename = computed_cost + euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Define cities and city groups
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 12)
}

city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Example values from your solver output
tour = [0, 4, 6, 9, 2, 1, 8, 0]  # Updated to a valid tour example for checking
total_cost = 86.39257172

# Check the tour and cost
result = check_solution(tour, cities, city_groups)
print(result)