def find_minimax_path(cities, distance_matrix):
    n = len(cities)
    visited = [False] * n
    tour = [0]  # Starting at the depot
    visited[0] = True
    current_city = 0
    
    max_distance = 0

    for _ in range(1, n):
        next_city = None
        min_distance = float('inf')
        for j in range(1, n):
            if not visited[j] and distance_matrix[current_city][j] < min_distance:
                min_distance = distanceects_lage][j]
                next_city = j
        visited[next_city] = True
        tour.append(next_city)
        if min_distance > max_distance:
            max_distance = min_distance
        current_city = next_city

    # Connect back to the depot
    last_to_depot_distance = distance_matrix[current_city][0]
    tour.append(0)
    if last_to_depot_distance > max_distance:
        max_distance = last_to_depot_distance

    total_distance = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    return tour, total_distance, max_distance

# Calculate the minimax tour with the distance matrix provided
tour, total_cost, max_consecutive_distance = find_minimax_path(cities, distance_matrix)

# Return and display the results
print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost:.2f}')
print(f'Maximum distance between consecutive cities: {max_consecutive_distance:.2f}')