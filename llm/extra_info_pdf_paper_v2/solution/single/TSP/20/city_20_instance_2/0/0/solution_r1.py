import math

# Define the cities' coordinates
cities = [
    (3, 26),   # Depot
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
    """ Compute Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(tour):
    """ Calculate the total distance of the tour. """
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def nearest_neighbor(start, cities):
    """ Generate an initial tour using the nearest neighbor heuristic. """
    unvisited = set(range(1, len(cities)))
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current], cities[city]))
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    return tour

def two_opt(tour):
    """ Improve the tour by iteratively performing 2-opt swaps. """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distance(cities[tour[i]], cities[tour[j]]) + distance(cities[tour[i-1]], cities[tour[j+1]]) < distance(cities[tour[i]], cities[tour[i-1]]) + distance(cities[tour[j]], cities[tour[j+1]]):
                    tour[i:j + 1] = reversed(tour[i:j + 1])
                    improved = True
    return tour

# Generate an initial tour using the nearest neighbor heuristic
initial_tour = nearest_neighbor(0, cities)
# Complete the tour by returning to the depot
complete_tour = initial_tour + [0]
# Apply 2-opt optimization to improve the tour
optimized_tour = two_opt(complete_tour)

# Calculate the total tour cost
total_cost = calculate_total_distance(optimized_tákou)

# Output the tour and the total cost
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost}")