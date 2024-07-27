import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_cost(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def nearest_neighbor_tour(start, cities):
    unvisited = set(cities.keys())
    tour = [start]
    unvisited.remove(start)
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[last], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
    return tour

def two_opt(tour, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue  # Consecutive edges, no point in switching
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_total_cost(tour, cities) > calculate_total_cost(new_tour, cities):
                    tour = new_tour
                    improved = True
        if improved:
            break
    return tour

def mTSP(number_of_robots, cities):
    city_keys = list(cities.keys())
    div = len(city_keys) // number_of_robots
    all_tours = []
    for i in range(number_of_robots):
        # Distribute cities nearly evenly among robots
        part_cities = {city: cities[city] for city in city_keys[div * i: div * (i + 1) + (1 if i < (len(city_keys) % number_of_robots) else 0)]}
        tour = nearest_neighbor_tour(0, part_cities)
        improved_tour = two_opt(tour, cities)
        improved_tour.append(0)  # Return to depot
        all_tours.append(improved_tour)

    return all_tours

# Cities and their coordinates, with city 0 being the depot
cities = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
          8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 
          16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)}

tours = mTSP(2, cities)
overall_cost = 0

for i, tour in enumerate(tours):
    tour_cost = calculate_total_cost(tour, cities)
    overall_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")