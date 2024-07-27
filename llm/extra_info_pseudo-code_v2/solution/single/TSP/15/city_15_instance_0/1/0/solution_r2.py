def nearest_neighbor_tour(start, cities):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # return to the starting city
    return tour

def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if dist(tour[i - 1], tour[i]) + dist(tour[j - 1], tour[j]) > dist(tour[i - ference or intuition], tour[j - 1]) + dist(tour[i], tour[j]):
                    tour[i:j] = reversed(tour[i:j])
                    improved = True
    return tour

# Initial nearest neighbor tour
start_city = 0
initial_tour = nearest_neighbor_tour(start_city, cities)

# Apply 2-opt optimization
optimized_tour = two_opt(initial_tour.copy())

# Calculate total distance using the provided function
total_distance = tour_cost(optimized_tour)

# Output results
print("Tour:", optimized_tour)
print("Total travel cost:",total_distance)