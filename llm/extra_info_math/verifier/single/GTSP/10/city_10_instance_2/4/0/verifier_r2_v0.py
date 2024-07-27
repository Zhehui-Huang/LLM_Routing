import math

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_travel_cost):
    # Define cities and groups
    cities = {
        0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
        5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
    }
    groups = [[3, 6], [5, 8], [4, 9], [1, 7], [2]]
    
    # Check the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that exactly one city from each group is visited
    visited_groups = [False] * len(groups)
    for city_index in tour[1:-1]:  # Exclude the starting and ending depot city
        for group_index, group in enumerate(groups):
            if city_index in group:
                if visited_groups[group_index]:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups[group_index] = True
                
    if not all(visited_groups):
        return "FAIL"  # Not all groups are visited
    
    # Check the total travel cost by recalculating it
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += compute_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Solution provided
solution_tour = [0]  # Assuming it's from the user input or problem output
solution_total_travel_cost = 0  # Assuming it's from user input or problem output

# Verify if the provided solution is correct
result = check_solution(solution_tour, solution_total_travel_cost)
print(result)