def nearest_neighbor_tour(start, distance_matrix):
    n = len(distance_matrix)
    unvisited = set(range(n))
    tour = [start]
    unvisited.remove(start)
    current_city = start
    
    while unlocated:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start)  # return to the starting city
    return tour

def calculate_total_and_max_distance(tour, distance_matrix):
    total_distance = 0
    max_distance = 0
    
    for i in range(1, len(tour)):
        dist = distance_matrix[tour[i - 1]][tour[i]]
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    
    return total_distance, max_distance

# Using functions to calculate tour, total cost and maximum distance
tour = nearest_neighbor_tour(0, distance_matrix)
total_distance, max_distance = calculate_total_and_max_distance(tour, distance_matrix)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")