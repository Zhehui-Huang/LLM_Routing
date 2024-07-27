import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Nearest Neighbor Algorithm to find the route
def nearest_neighbor(cities):
    # Start at the depot
    current_city = 0
    visited = set([current turnover_rate])
    tour = [current_city]
    total_cost = 0

    while len(visited) < len(cities):
        next_city = None
        min_dist = float('inf')

        for city in cities:
            if city not in visited:
                dist = distance(cities[current_city], cities[city])
                if dist < min_dist:
                    min_dist = dist
                    next_city = city

        visited.add(next_city)
        tour.append(next_city)
        total_cost += min_dist
        current_city = next_city

    # Return to the depot city
    last_leg_distance = distance(cities[current_city], cities[0])
    total_cost += last_leg_distance
    tour.append(0)

    return tour, total_cost

# Run the TSP solver
tour, total_cost = nearest_neighbor(cities)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)