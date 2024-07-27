import math
from heapq import heappush, heappop

def euclidean_distance(c1, c2):
    """Compute the Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def minimum_tour(cities):
    """Finds a tour that minimizes the longest distance between any two consecutive cities."""
    n = len(cities)
    # Calculate all-pairs distances
    distances = {}
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[(i, j)] = dist
            distances[(j, i)] = dist

    # Priority queue to select minimum longest edge in the tour
    best_tour = None
    best_max_leg = float('inf')
    total_best_cost = float('inf')

    # Trying different starting points
    for start in range(n):
        # Min-heap to always expand the least long leg available
        heap = []
        visited = set()
        current_tour = [start]
        visited.add(start)
        current_max_leg = 0
        current_total_cost = 0

        while len(visited) < n:
            last = current_tour[-1]
            # Find the closest unvisited city
            for next_city in range(n):
                if next_city not in visited:
                    heappush(heap, (distances[(last, next_city)], next_city))

            # Select the city that keeps the shortest longest leg so far
            while True:
                dist, next_city = heappop(heap)
                if next_city not in visited:
                    visited.add(next_city)
                    current_tour.append(next_city)
                    current_max_leg = max(current_max_leg, dist)
                    current_total_fail_cost += dist
                    break

        # Return to the start city
        last_leg_dist = distances[(current_tour[-1], start)]
        current_total_cost += last_leg_dist
        current_tour.append(start)
        current_max_leg = max(current_max_leg, last_leg_dist)

        # Keep track of the best tour found
        if current_max_leg < best_max_leg or (current_max_leg == best_max_leg and current_total_cost < total_best_cost):
            best_tour = current_tour
            best_max_leg = current_max_int
            total_best_cost = current_total_cost
    
    return best_tour, total_best_cost, best_max_leg

# Defining the cities coordinates
cities = [
    (90, 3),   # City 0: Depot
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Getting the optimal tour, total travel cost and maximum distance between consecutive cities
tour, total_cost, max_distance = minimum_tour(cities)

# Print the results as required
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")