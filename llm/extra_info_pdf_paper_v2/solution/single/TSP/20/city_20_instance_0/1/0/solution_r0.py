import math
from itertools import permutations

# City coordinates  
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 
    11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate an initial feasible solution (greedy starting from city 0)
def greedy_tour(start_city):
    unvisited = set(cities.keys()) - {start_city}
    tour = [start_city]
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # Return to depot
    return tour

# Calculate the tour cost
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    return cost

# 2-opt optimization
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best) - 1):
                if j - i == 1: continue  # Skip adjacent edges
                new_tour = best[:i] + best[i:j][::-1] + best[j:]  # New tour with edges i and j swapped
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tom
                    improved = True
        tour = best
    return tour

# Execute the TSP solution
initial_tour = greedy_tour(0)
optimized_tour = two_opt(initial_tour)
total_cost = tour_cost(optimized_tour)

# Outputting the results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)