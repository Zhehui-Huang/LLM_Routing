def verify_tsp_solution(tour, total_cost):
    def euclidean_distance(city1, city2):
        return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) ** 0.5

    # Given city coordinates from the problem description.
    cities = [
        (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
        (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
        (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
    ]
    
    # Verify the robot starts and ends at the depot (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify that each city is visited exactly once.
    visited = set(tour[1:-1])  # Exclude the depot city at the start and end.
    if len(visited) != len(cities) - 1 or any(i not in visited for i in range(1, len(cities))):
        return "FAIL"
    
    # Verify there are no subtours.
    visited_check = set()
    for i in range(len(tour) - 1):
        if tour[i] in visited_check:
            return "FAIL"
        visited_check.add(tour[i])

    # Calculate the total tour cost and verify it.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if abs(calculated_cost - total_cost) > 1e-5:
        return "FAIL"

    return "CORRECT"

# Provided result
tour = [0, 10, 0, 9, 6, 7, 1, 11, 2, 3, 5, 13, 12, 4, 14, 8, 0]
total_cost = 727.6272686573534

# Verify if the provided solution meets all the requirements.
verification_result = verify_tsp_solution(tour, total_cost)
print(verification_result)