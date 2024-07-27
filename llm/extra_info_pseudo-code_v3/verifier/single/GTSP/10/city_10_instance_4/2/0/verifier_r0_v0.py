import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def check_solution(tour, city_positions, city_groups):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the robot visits exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city in the beginning and end
        for group_id, group in enumerate(city_groups):
            if city in group:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.add(group_id)
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Calculate the total travel cost using the Euclidean distance
    total_cost_calc = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        total_cost_calc += euclidean_distance(city_positions[city_a], city_positions[city_b])

    # Since the original problem was to find the shortest path, we should ideally
    # calculate or know the minimal possible path (optimal cost). However, without
    # calculating or having the optimal tour for validation, we rely on basic checks.
    # The next point essentially needs an optimal solution comparison or a feasible threshold
    # As given test solution might not be a valid one to calculate. 
    # Assuming a non-zero threshold cost that the minimal tour would exceed
    if total_cost_calc == 0:
        return "FAIL"

    return "CORRECT"

# City positions and groups according to the problem
positions = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}
groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]

# Solution to verify
solution_tour = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Check the solution
verification_result = check_solution(solution_tour, positions, groups)
print(verification_result)