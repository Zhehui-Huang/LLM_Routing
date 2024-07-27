import math

# Cities data
cities = [
    (9, 93),   # City 0 - Depot
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tsp(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]  # start at the depot
    visited[0] = True
    total_cost = 0

    current_city = 0

    while len(tour) < n:
        next_city = None
        min_distance = float('inf')
        for i in range(n):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    next_city = i
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_distance
        current_city = next_city

    # Return to depot
    return_to_depot_distance = euclidean_distance(cities[current_city], cities[0])
    total_cost += return_to_depot_distance
    tour.append(0)

    return tour, total_cost

tour, total_cost = nearest_neighbor_tsp(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")