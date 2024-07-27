import math

# Coordinates of all cities including depot city 0
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def find_tour():
    # Initialize tour starting at the depot city 0
    tour = [0]
    num_cities = len(cities)
    visited = [False] * num_cities
    visited[0] = True

    # Proceed until the tour includes all cities returning to the depot
    while len(tour) < num_cities:
        last = tour[-1]
        next_city = None
        min_distance = float('inf')
        
        for i in range(num_cities):
            if not visited[i]:
                dist = distance(last, i)
                if dist < min_distance:
                    min_distance = dist
                    next_city = i

        visited[next_city] = True
        tour.append(next_city)

    # Return to the starting city (depot)
    tour.append(0)

    # Calculate total travel cost and maximum distance
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    return tour, total_cost, max_distance

# Find optimal tour using the heuristic
tour, total_cost, max_distance = find_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")