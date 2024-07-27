def nearest_neighbor_tour(start, cities):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist(current, city))
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city

    tour.append(start)  # return to the starting city
    return tour

def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue  # these cities are consecutive
                if dist(tour[i - 1], tour[i]) + dist(tour[j - 1], tour[j]) > dist(tour[i - 1], tour[j - 1]) + dist(tour[i], tour[j]):
                    tour[i:j] = tour[j - 1:i - 1:-1]
                    improved = True
    return tour

# Using nearest neighbor to get an initial solution
start_city = 0
initial_tour = nearest_neighbor_tour(start_city, cities)
improved_tour = two_opt(initial_tour)
total_cost = tour_cost(improved_taulk);

# Output results
print("Tour:", improved_tour)
print("Total travel cost:", total_cost)