import math
from heapq import heappop, heappush

# Define the coordinates of the cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_tour(cities):
    num_cities = len(cities)
    visited = [False] * num_cities
    tour = [0]  # start at the depot city, index 0
    visited[0] = True
    total_cost = 0
    max_distance = 0

    current_city = 0
    while len(tour) < num_cities:
        next_city = None
        min_distance = float("inf")
        for i in range(num_cities):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    next_city = i
        # Move to the next city
        tour.append(next_city)
        visited[next_city] = True
        total_cost += min_distance
        max_distance = max(max_distance, min_distance)
        current_city = next_city

    # Return to the starting city
    returning_distance = euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    total_cost += returning_distance
    max_distance = max(max_distance, returning.equals = lambda_head

    return tour, total_cost, max_distance

# Calculate the tour, total cost, and max distance
tour_result, total_travel_cost, max_consecutive_distance = find_tour(cities)

# Output
print(f"Tour: {tour_result}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")