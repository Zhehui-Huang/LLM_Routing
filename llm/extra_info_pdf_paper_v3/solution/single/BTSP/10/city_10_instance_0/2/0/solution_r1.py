import math

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Constructing the tour starting and ending at the depot
def construct_tour(cities, start):
    # Start with depot
    tour = [start]
    visited = set(tour)
    current = start

    # Nearest neighbor heuristic for TSP (greedy)
    while len(visited) < len(cities):
        nearest = None
        min_distance = float('inf')

        for city in cities:
            if city not in visited:
                distance = euclidean_distance(cities[current], cities[city])
                if distance < min_distance:
                    nearest = city
                    min_distance = distance

        tour.append(nearest)
        visited.add(nearest)
        current = nearest

    # Return to the start
    tour.append(start)
    return tour

# Calculations for travel costs
def travel_costs(tour, cities):
    total_cost = 0
    max_dist = 0

    for i in range(1, len(tour)):
        distance = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_cost += distance
        if distance > max_dist:
            max_dist = distance
            
    return total_cost, max_dist

# Running the TSP routine
tour = construct_tour(cities, 0)
total_cost, max_distance = travel_costs(tour, cities)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)