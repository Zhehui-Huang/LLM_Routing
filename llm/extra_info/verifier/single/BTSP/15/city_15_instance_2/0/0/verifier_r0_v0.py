def test_solution(tour, total_travel_cost, max_distance):
    # Requirements checking
    # [Requirement 1] The tour must start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Must visit each city exactly once
    unique_cities_visited = set(tour[1:-1])  # Excludes the repeated depot city at the end
    if len(unique_cities_visited) != 14 or any(city not in unique_cities_visited for city in range(1, 15)):
        return "FAIL"
    
    # [Requirement 3] Minimize the maximum distance between any two consecutive cities
    # This is dependent on the provided solution to check whether it's actually minimized.
    # Testing if the consecutive maximum distance provided is accurate with a trivial check since actual minimum cannot be inferred without solving problem.
    consecutive_max_distance = 0
    coordinates = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
        (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
    ]
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        consecutive_max_distance = max(consecutive_max_distance, dist)

    if max_distance != consecutive_max_distance:
        return "FAIL"
    
    return "CORRECT"

# Test the provided solution
tour = [0, 1, 2, 3, 4, 0]
total_travel_cost = 0.0
max_distance = 0
print(test_solution(tour, total_travel_cost, max_distance))