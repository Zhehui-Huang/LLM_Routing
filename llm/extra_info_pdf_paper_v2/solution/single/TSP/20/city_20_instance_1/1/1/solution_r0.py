import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_tour_cost(tour, cities):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

def nearest_neighbor(cities, start):
    unvisited = set(cities.keys())
    tour = [start]
    unvisited.remove(start)
    
    current_city = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start)  # return to depot
    return tour

def two_opt(tour, cities):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # neighbors, no gain.
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_tour_cost(new_tour, cities) < total_tour_cost(best, cities):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Define the cities based on the given coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79), 
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Apply Nearest Neighbor to get an initial tour
initial_tour = nearest_neighbor(cities, 0)

# Apply 2-opt on the initial tour to optimize it
optimized_tour = two_opt(initial_tour, cities)

# Calculate the cost of the optimized tour
tour_cost = total_tour_cost(optimized_tour, cities)

# Output the result
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {tour_cost}")