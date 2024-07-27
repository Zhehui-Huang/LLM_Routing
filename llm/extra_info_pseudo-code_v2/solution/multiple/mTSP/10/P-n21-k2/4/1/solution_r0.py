import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour, cities):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return cost

def nearest_neighbor_tour(start, cities, available_cities):
    tour = [start]
    current_city = start
    while len(available_cities) > 0:
        next_city = min(available_cities, key=lambda x: euclidean_distance(cities[current_city], cities[x]) + (euclidean_distance(cities[x], cities[start]) / 2))
        available_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    tour.append(start)
    return tour

def two_opt(tour, cities):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_tour_cost(new_tour, cities) < total_tour_cost(best, cities):
                    best = new_tour
                    improved = True
        tour = best
    return best

def mTSP(cities, num_robots):
    assignment = [[] for _ in range(num_robots)]
    available_cities = list(range(1, len(cities)))
    
    # Assign cities to robots
    while available_cities:
        for i in range(num_robots):
            if available_cities:
                assignment[i].append(available_cities.pop(0))

    tours = []
    for i in range(num_robots):
        tour = nearest_neighbor_tour(0, cities, assignment[i])
        optimized_tour = two_opt(tour, cities)
        tours.append(optimized_tour)

    return tours

# Define cities coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
          (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

num_robots = 2
tours = mTSP(cities, num_robots)
total_cost = 0

for idx, tour in enumerate(tours):
    cost = total_tour_cost(tour, cities)
    total_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")