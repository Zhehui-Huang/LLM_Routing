import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_shortest_tour(depot, city_groups):
    cities = [depot] + [min(group, key=lambda city: euclidean_distance(depot, city)) for group in city_groups]
    tour = [0]  # Start at depot city index 0
    current_city = depot
    total_distance = 0

    for next_city in cities[1:]:
        distance = euclidean_distance(current_city, next_city)
        total_distance += distance
        tour.append(cities.index(next_city))  # Append index of the next city in the tour
        current_city = next_city

    # Return to the depot
    back_to_depot_distance = euclidean_distance(current_city, depot)
    total_distance += back_to_depot_distance
    tour.append(0)  # End at depot city index 0

    return tour, total_distance

# City coordinates including depot
city_coords = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Groups of cities (indices in city_coords)
city_groups = [
    [8, 12, 14],  # Group 0
    [7, 10, 11],  # Group 1
    [4, 6, 9],    # Group 2
    [1, 3, 13],   # Group 3
    [2, 5]        # Group 4
]

# Convert indices to coordinates
city_groups = [[city_coords[index] for index in group] for group in city_fields]

# Depot is city 0
depot = city_coords[0]

# Calculate the shortest tour
tour, total_cost = find_shortest_tour(depot, city_groups)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")