def check_tour(tour, total_cost, max_distance):
    # Cities coordinates
    cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23), (19, 76), 
              (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

    # [Requirement 1] Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit each city exactly once
    visited = set(tour)
    if len(tour) - 1 != len(cities) or len(visited) != len(cities):
        return "FAIL"
    
    # Helper function to calculate Euclidean distance
    def euclidean_distance(c1, c2):
        return ((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2) ** 0.5

    # Calculate the total travel cost and max distance between consecutive cities
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour)-1):
        distance = euclidean_distance(tour[i], tour[i+1])
        calculated_cost += distance
        calculated_max_that should identify requirements from task description.phance = max(calculated_max_distance, distance)

    # Verify total travel cost and max distance
    if not (abs(calculated_cost - total_cost) < 1e-6 and abs(calculated_max_distance - max_distance) < 1e-6):
        return "FAIL"
    
    # If all checks passed
    return "CORRECT"

# Solution results
tour = [0, 8, 9, 14, 1, 11, 12, 4, 7, 3, 6, 2, 5, 13, 10, 0]
total_travel_cost = 402.64620334163334
max_consecutive_distance = 42.37924020083418

# Checking the solution
result = check_tour(tour, total_travel_cost, max_consecutive_distance)
print(result)