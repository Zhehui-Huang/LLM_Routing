import math

# Define the cities' coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Nearest Neighbor heuristic to find an initial solution
def nearest_neighbor(start=0):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    tour.append(start)  # returning to the depot
    return tour

# 2-opt swap heuristic to improve the tour
def two_opt(tour):
    best = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best) - 1):
                if j - i == 1:
                    continue  # Skip adjacent edges
                new_tour = best[:i] + best[i:j][::-1] + best[j:]
                if sum(distance(new_tour[k], new_tour[k + 1]) for k in range(len(new_tour) - 1)) < \
                   sum(distance(best[k], best[k + 1]) for k in range(len(best) - 1)):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Construct the initial tour and improve it
init_tour = nearest_neighbor()
final_tour = two_opt(init_tour)

# Output the tour and the total travel cost
total_cost = sum(distance(final_tour[i], final_tour[i + 1]) for i in range(len(final_tour) - 1))
print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost}")