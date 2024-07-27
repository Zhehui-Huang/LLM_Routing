import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def nearest_neighbor(start_city, cities):
    unvisited = set(cities.keys()) - {start_city}
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # returning to the depot
    return tour

def calculate_total_distance(tour, cities):
    return sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Define cities and their positions
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 408), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Find the shortest path using Nearest Neighbor heuristic
tour = nearest_neighbor(0, cities)
total_travel_cost = calculate_total_distance(tour, cities)

# Display results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)