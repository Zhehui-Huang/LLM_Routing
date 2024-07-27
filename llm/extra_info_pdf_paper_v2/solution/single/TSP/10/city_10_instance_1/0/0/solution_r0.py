import numpy as np
import math

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def nearest_neighbor(start_city, cities):
    tour = [start_city]
    remaining_cities = list(cities.keys())
    remaining_cities.remove(start_city)
    
    current_city = start_city
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # returning to the starting point
    return tour

# Initial tour creation
tour = nearest_neighbor(0, cities)

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def two_opt(tour, cities):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # adjacent edges
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_total_travel_cost(new_tour, cities) < calculate_total_travel_cost(tour, cities):
                    tour = new_tour
                    improvement = True
        return tour

# Optimizing the tour using 2-opt
opt_tour = two_opt(tour, cities)
total_cost = calculate_total_travel_cost(opt_tour, cities)

print(f"Tour: {opt_tour}")
print(f"Total travel cost: {total_cost:.2f}")