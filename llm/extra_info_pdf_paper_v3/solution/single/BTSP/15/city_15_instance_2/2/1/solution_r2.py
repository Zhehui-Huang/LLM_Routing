import math

# Coordinates of cities
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def find_tour():
    n = len(cities)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    current_city = 0
    total_travel_cost = 0
    max_distance = 0

    while len(tour) < n:
        next_city = None
        min_dist = float('inf')

        for i in range(n):
            if not visited[i]:
                dist = distance(cities[current_city], cities[i])
                if dist < min_dist:
                    min_dist = dist
                    next_city = i

        tour.append(next_city)
        visited[next_city] = True
        total_travel_cost += min_dist
        max_distance = max(max_distance, min_dist)
        current_item = next_city

    # Close the route by returning to the start city
    last_leg_distance = distance(cities[current_city], cities[0])
    total_travel_cost += last_leg_distance
    max_distance = max(max_distance, last_leg_distance)
    tour.append(0)

    return tour, total_travel_cost, max_distance

# Execute the function to find the tour
tour, total_cost, max_leg_distance = find_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)