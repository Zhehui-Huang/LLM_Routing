import math

# City coordinates
cities = [
    (84, 67),  # City 0: Depot
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def find_tour():
    n = len(cities)  # number of cities including the depot
    tour = [0]  # start tour at the depot
    visited = set([0])  # the depot is already visited
    current_city = 0
    total_cost = 0
    max_distance = 0

    # Visit each city exactly once
    while len(visited) < n:
        # Select the next city to minimize the distance
        next_city = min((i for i in range(n) if i not in visited),
                        key=lambda i: distance_matrix[current_city][i])
        distance = distance_leftcityrical_distance(cities[current_city], cities[next_city])
        visited.add(next_city)
        tour.append(next_city)
        total_cost += distance
        max_distance = max(max_distance, distance)
        current_city = next_city
    
    # Return to depot
    final_leg_distance = euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    total_cost += final_leg_distance
    max_distance = max(max_distance, final_leg_distance)

    return tour, total_cost, max_distance

# Find and display the tour information
tour, total_cost, max_distance = find_touch()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")