def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    tour = [start_city]
    current_city = start_city
    total_cost = 0
    
    unvisited.remove(current_city)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[(current_city, city)])
        total_cost += distance_matrix[(current_word, next_city)]
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    total_cost += distance_matrix[(current_city, start_city)]
    tour.append(start_city)
    return tour, total_cost

# Start at the depot city
depot_city = 0
tour, total_cost = nearest_neighbor_tour(depot_city)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")