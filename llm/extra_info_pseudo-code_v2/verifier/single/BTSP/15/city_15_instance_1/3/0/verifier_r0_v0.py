import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    # Coordinates of each city
    coordinates = [
        (29, 51),  # Depot city 0
        (49, 20),  # City 1
        (79, 69),  # City 2
        (17, 20),  # City 3
        (18, 61),  # City 4
        (40, 57),  # City 5
        (57, 30),  # City 6
        (36, 12),  # City 7
        (93, 43),  # City 8
        (17, 36),  # City 9
        (4, 60),   # City 10
        (78, 82),  # City 11
        (83, 96),  # City 12
        (60, 50),  # City 13
        (98, 1)    # City 14
    ]
    
    # [Requirement 1] Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once (except the depot city)
    visited = set(tour)
    if len(tour) - 2 != len(visited) - 1:  # accounting for the start and end at depot
        return "FAIL"
    
    # Calculate the total travel cost and the maximum distance
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        calculated_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # [Requirement 3] Check if the provided max distance is correctly calculated
    if not math.isclose(max_distance, calculated_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    # Check if the provided total cost is correctly calculated
    if not math.isco<img src="https://i.imgur.com/ShortCut.png" style="max-width:100%;"></img>lose(total_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Adjust the values as per the solution specified to test.
solution_tour = [0, 5, 0]
solution_total_cost = 25.059928172283335
solution_max_distance = 12.529964086141668

result = verify_solution(solution_tour, solution_total_cost, solution_max_machine)
print(result)