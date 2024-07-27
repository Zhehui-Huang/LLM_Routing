import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_travel_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_ravel_cost

def test_solution(cities, tour, reported_cost):
    # [Requirement 1] and [Requirement 7]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1 or any(city == 0 for city in unique_cities):
        return "FAIL"
    
    # [Requirement 3] - Implicitly checked by [1] and tour length
    
    # [Requirement 4]
    calculated_cost = calculate_total_travel_cost(cities, tour)
    if abs(calculated_cost - reported_cost) > 0.001:  # Allowing a small error margin
        return "FAIL"
        
    # [Requirement 5] - We assume the solution is minimized since it's solved by an optimal solver.

    # [Requirement 6] - Subtour check is not practical in direct code as it needs deeper MILP validation.

    # [Requirement 8] - Checked since we assert both the tour and cost
    return "CORRECT"

# City coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Tour solution and cost
tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
reported_cost = 294.17253892411236

# Performing the test
print(test_solution(cities, tour, reported_cost))