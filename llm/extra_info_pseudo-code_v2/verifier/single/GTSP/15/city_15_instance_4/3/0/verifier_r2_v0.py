import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost):
    # Given Coordinates of the cities
    coordinates = [
        (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
        (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
        (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
    ]
    
    # Given groups and must visit exactly one from each
    groups = [
        [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
    ]
    
    # Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each group is represented exactly once in the tour
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:  # exclude the starting and ending depot, which should be 0
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
                
    if any(count != 1 for count in visited_groups):
        return "FAIL"

    # Calculate the total travel cost and compare it with the given total_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Example tour and its cost provided
input_tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
input_total_cost = 220.73043826129523

# Verify the solution
result = verify_solution(input_tour, input_total_cost)
print(result)  # Output "CORRECT" if everything is in order, otherwise "FAIL"