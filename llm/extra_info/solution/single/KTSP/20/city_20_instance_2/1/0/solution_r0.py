import math

# City coordinates (Index corresponds to city number)
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_shortest_tour():
    n_cities = len(cities)
    visited = [False] * n_cities
    tour = [0]  # Start at the depot city
    visited[0] = True
    current_city = 0
    total_cost = 0

    while len(tour) < 10:
        # Find the nearest non-visited city
        next_city = None
        min_distance = float('inf')
        for i in range(n_cities):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    next_city = i
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_distance
        current_city = next_city
    
    # Return to the depot city
    return_to_depot_cost = euclidean_distance(cities[current_city], cities[0])
    total_cost += return_to_depot_cost
    tour.append(0)  # Complete the tour by returning to the depot

    return tour, total_cost

# Get the shortest tour and its total cost
tour, total_cost = find_shortest_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))