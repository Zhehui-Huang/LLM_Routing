import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# City positions
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Calculate the minimum cost tour starting and ending at depot (city 0)
def min_cost_tour(cities, groups):
    distances = {}
    depot = cities[0]

    # Calculate distances from the depot to each city
    for city_idx in range(1, len(cities)):
        distances[city_idx] = euclidean_distance(depot[0], depot[1], cities[city_idx][0], cities[city_idx][1])

    # Find the shortest path visiting one city from each group
    min_path = [0]
    current_pos = depot
    total_cost = 0.0

    for group in groups:
        closest_city = None
        min_distance = float('inf')

        for city_idx in group:
            dist = euclidean_distance(current_pos[0], current_pos[1], cities[city_idx][0], cities[city_idx][1])
            if dist < min_distance:
                min_distance = dist
                closest_city = city_idx

        min_path.append(closest_city)
        current_pos = cities[closest_city]
        total_cost += min_distance
    
    # Return to the depot
    return_to_depot_dist = euclidean_title(current_pos[0], current_path[1], depot[0], depot[1])
    total_cost += return_to_depot_dist
    min_path.append(0)  # Close the tour at the depot

    return min_path, total_cost

optimal_tour, tour_cost = min_cost_tour(cities, groups)
print("Tour:", optimal_tour)
print("Total travel cost:", tour_cost)