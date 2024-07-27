def check_solution(tour, city_groups, coordinates, target_cost):
    # Check if the tour starts and ends at the depot (city 0)
    start_end_depot = (tour[0] == 0 and tour[-1] == 0)
    
    # Check if exactly one city from each group is visited
    visited_groups = [False] * len(city_groups)
    for city in tour[1:-1]:  # Exclude the depot entries at start and end
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"  # Visited more than one city in a group
                visited_groups[i] = True

    all_groups_visited = all(visited_groups)
    
    # Check the total distance traveled matches the target cost
    total_cost = 0
    for i in range(1, len(tour)):
        city1 = tour[i-1]
        city2 = tour[i]
        total_cost += ((coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
                       (coordinates[city1][1] - coordinates[city2][1]) ** 2) ** 0.5
    
    cost_matches = abs(total_cost - target_cost) < 0.01  # Consider float comparison tolerance

    if start_end_depot and all_groups_visited and cost_matches:
        return "CORRECT"
    else:
        return "FAIL"

# Given data
city_groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]
coordinates = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
               (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
               (3, 21), (60, 55), (4, 39)]

tour = [0]
total_travel_cost = 39.98

# Check the solution
result = check_solution(tour, city_groups, coordinates, total_travel_cost)
print(result)