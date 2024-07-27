import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def find_tour(cities):
    n = len(cities)
    visited = [False] * n
    visited[0] = True
    tour = [0]
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
        current_city = next_city

    # Returning to the starting point (depot city)
    tour.append(0)

    # Calculate the total travel cost and maximum distance between consecutive cities
    total_distance = 0
    max_distance_between_cities = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_distance += distance
        if distance > max_distance_between_cities:
            max_distance_between_cities = distance

    return tour, total_distance, max_distance_between_cities

# Defining the city coordinates
cities = [
    (26, 60),  # Depot city 0
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

# Calculating the tour details
tour, total_cost, max_distance = find_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)