import math

# Define the cities' coordinates
cities = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

def distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(tour):
    """Calculate the total distance of the tour that starts and ends at the depot."""
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance(cities[tour[i]], cities[tour[i + 1]])
    return total_dist

# Nearest Neighbor Heuristic to generate an initial tour
def nearest_neighbor(start, cities):
    tour = [start]
    available_cities = set(range(len(cities))) - {start}

    while available_cities:
        last_city = tour[-1]
        next_city = min(available_cities, key=lambda city: distance(cities[last_city], cities[city]))
        tour.append(next_city)
        available_cities.remove(next_city)

    tour.append(start)  # Return to the depot
    return tour

# 2-opt optimization algorithm
def two_opt(tour):
    def swap(tour, i, j):
        return tour[:i] + tour[i:j+1][::-1] + tour[j+1:]

    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j-i == 1: continue  # Skip consecutive nodes
                if distance(cities[tour[i]], cities[tour[i-1]]) + distance(cities[tour[j]], cities[tour[j+1]]) > distance(cities[tour[i]], cities[tour[j]]) + distance(cities[tour[i-1]], cities[tour[j+1]]):
                    tour = swap(tour, i, j)
                    made_improvement = True
    return tour

# Generate the initial tour and optimize it
initial_tour = nearest_neighbor(0, cities)
optimized_tour = two_opt(initial_tour)
optimized_distance = total_distance(optimized_tour)

# Output the results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_distance}")