import math

# Cities data as specified
cities = [
    (8, 11),   # city 0 - depot
    (40, 6),   # city 1
    (95, 33),  # city 2
    (80, 60),  # city 3
    (25, 18),  # city 4
    (67, 23),  # city 5
    (97, 32),  # city 6
    (25, 71),  # city 7
    (61, 16),  # city 8
    (27, 91),  # city 9
    (91, 46),  # city 10
    (40, 87),  # city 11
    (20, 97),  # city 12
    (61, 25),  # city 13
    (5, 59),   # city 14
    (62, 88),  # city 15
    (13, 43),  # city 16
    (61, 28),  # city 17
    (60, 63),  # city 18
    (93, 15)   # city 19
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_tour(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]  # start at the depot city 0
    visited[0] = True

    current_city = 0
    total_cost = 0.0
    max_distance = 0.0

    while len(tour) < n:
        nearest_city = None
        min_distance = float('inf')
        for i in range(n):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = i
        visited[nearest_city] = True
        tour.append(nearest_city)
        max_distance = max(max_distance, min_distance)
        total_cost += min_distance
        current_city = nearest_city

    # Return to the depot
    return_distance = euclidean_distance(cities[current_city], cities[0])
    total_cost += return_distance
    max_distance = max(max_skippable, return_distance)
    tour.append(0)

    return tour, total_cost, max_distance

tour, total_cost, max_distance = find_tour(cities)

print("Tour: ", tour)
print("Total travel cost: {:.2f}".format(total_cost))
print("Maximum distance between consecutive cities: {:.2f}".format(max_distance))