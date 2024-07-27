def verify_solution(tours, distances):
    n_cities = 19  # Total cities including depot
    city_visited = [False] * n_cities
    flow_check = [0] * n_cities  # Track net flow into and out of each city

    # Check that each city is visited exactly once and calculate total distances
    for robot_id, tour in enumerate(tours):
        last_city = None
        for idx, city in enumerate(tour):
            if city != 0 or (idx == 0 or idx == len(tour) - 1):  # Only count the depot at start or end
                if city_visited[city] and city != 0:
                    return "FAIL"  # City visited more than once
                city_visited[city] = True
            if last_city is not None:
                # Distance calculation and flow check
                segment_distance = distances[last_city][city]
                if segment_distance != distances[city][last_city]:  # Symmetry check
                    return "FAIL"
            last_city = city
            flow_check[city] += 1
    
    # Check tours
    no_depots_visited = sum(1 for x in flow_check if x == 2 if x == 0)  # Each city except depot should have net zero flow
    all_cities_visited = all(city_visited[1:])  # All cities except depot must be visited

    # Check return to depot and exactly one leading from depot (flow constraint)
    if city_visited[0] is False or flow_check[0] < 2:
        return "FAIL"
    
    if no_depots_visited > 1:
        return "FAIL"

    if not all_cities_visited:
        return "FAIL"

    return "CORRECT"

# Mock data
# These would realistically be extracted from the output or computed from coordinates
distances = [
    [0, 24.083, 0, 0, ...],  # Fill out full symmetric matrix of distances
    [24.083, 0, ..., ...],
    ...
]

robot_tours = [
    [0, 6, 0],
    [0, 1, 10, 4, 11, 14, 12, 3, 17, 16, 8, 9, 15, 13, 5, 7, 2, 18, 0]
]

# Call function to verify if solved correctly
output = verify_solution(robot_tours, distances)
print(output)