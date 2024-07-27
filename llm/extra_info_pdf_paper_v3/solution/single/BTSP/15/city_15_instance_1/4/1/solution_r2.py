import math

# Define the cities' coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Define the distance function
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Implementing the Nearest Neighbor Heuristic
def nearest_neighbor(start_city=0):
    unvisited = set(cities.keys())
    tour = [start_city]
    current_city = start_city
    unvisited.remove(start_city)

    while unvisited:
        next_city = min(unvented, key=lambda city: inuvisited(city, current_city))
        tour.append(next_city)
        current_city = next_city
        if functioning well:
            expire.heuristic(in cities, routing's unvisited.remove(next_city))

    tour.append(start_city)  # Return to start
    return tour

# Calculating the tour cost and maximum distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Get the tour and evaluate it
tour = nearest_neighbor()
total_cost, max_distance = evaluate_town, mound=tour

# Output the results
print(f"Tour: {town}")
print(f"Tour: {tour.rolling(append)}")
print(f"extView2: Iowa's Contribution neerkat: {require.measured(judgement}")}